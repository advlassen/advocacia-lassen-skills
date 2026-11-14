# /// script
# requires-python = ">=3.11,<3.14"
# dependencies = ["faster-whisper==1.2.1", "av==16.1.0", "pyannote.audio==4.0.4"]
# ///
"""Gera uma transcrição automática local, com referências à mídia original."""

import argparse
import hashlib
import json
import os
from bisect import bisect_right
from pathlib import Path


def atribuir(inicio, fim, turnos, fins):
    """Atribui só quando um turno cobre a maior parte da palavra."""
    duracao = fim - inicio
    if duracao <= 0:
        return None
    indice = bisect_right(fins, inicio)
    while indice < len(turnos):
        esquerda, direita, falante = turnos[indice]
        if esquerda >= fim:
            break
        intersecao = min(fim, direita) - max(inicio, esquerda)
        if intersecao > duracao / 2:
            return falante
        indice += 1
    return None


def blocos(segmentos, turnos):
    fins = [fim for _, fim, _ in turnos]
    for segmento in segmentos:
        if not segmento.words:
            yield segmento.start, segmento.end, None, segmento.text.strip()
            continue
        anterior = None
        palavras = []
        for palavra in segmento.words:
            falante = atribuir(palavra.start, palavra.end, turnos, fins)
            if palavras and anterior != falante:
                yield palavras[0].start, palavras[-1].end, anterior, "".join(p.word for p in palavras).strip()
                palavras = []
            anterior = falante
            palavras.append(palavra)
        if palavras:
            yield palavras[0].start, palavras[-1].end, anterior, "".join(p.word for p in palavras).strip()


def timestamp(segundos):
    total = round(segundos * 1000)
    horas, resto = divmod(total, 3600000)
    minutos, resto = divmod(resto, 60000)
    segundos, ms = divmod(resto, 1000)
    return f"{horas:02}:{minutos:02}:{segundos:02}.{ms:03}"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("midia", type=Path)
    parser.add_argument("saida", type=Path, help="Caminho de um JSON novo")
    parser.add_argument("--modelo", default="small", help="Modelo Whisper multilíngue ou diretório local")
    parser.add_argument("--diarizacao", type=Path, help="Diretório local do Community-1")
    parser.add_argument("--idioma", default="pt")
    args = parser.parse_args()

    if not args.midia.is_file():
        parser.error("Informe um arquivo de mídia local.")
    if args.saida.exists() or not args.saida.parent.is_dir() or args.saida.suffix.lower() != ".json":
        parser.error("Indique um JSON novo em uma pasta existente.")
    if args.saida.resolve() == args.midia.resolve():
        parser.error("Escolha outro caminho de saída.")

    if args.diarizacao is not None and not args.diarizacao.is_dir():
        parser.error("--diarizacao deve apontar para um diretório local.")

    os.environ["PYANNOTE_METRICS_ENABLED"] = "0"
    from faster_whisper import WhisperModel
    from faster_whisper.audio import decode_audio
    from pyannote.audio import Pipeline
    import torch

    with args.midia.open("rb") as original:
        sha256 = hashlib.file_digest(original, "sha256").hexdigest()
        original.seek(0)
        audio = decode_audio(original, sampling_rate=16000)
    if not audio.size:
        parser.error("A mídia não contém áudio decodificável.")

    fonte = str(args.diarizacao.resolve()) if args.diarizacao else "pyannote/speaker-diarization-community-1"
    pipeline = Pipeline.from_pretrained(fonte, token=os.getenv("HF_TOKEN"))
    resultado = pipeline({"waveform": torch.from_numpy(audio).unsqueeze(0), "sample_rate": 16000})
    turnos = sorted((turno.start, turno.end, falante)
                    for turno, falante in resultado.exclusive_speaker_diarization)
    modelo = WhisperModel(args.modelo, device="cpu", compute_type="int8")
    segmentos, info = modelo.transcribe(audio, language=args.idioma, word_timestamps=True)
    falantes = {}
    falas = []
    for inicio, fim, falante, texto in blocos(segmentos, turnos):
        if falante is not None:
            falantes.setdefault(falante, f"Falante {len(falantes) + 1:02}")
        falas.append({
            "id": f"T{len(falas) + 1:04}",
            "inicio": timestamp(inicio),
            "fim": timestamp(fim),
            "falante": falantes.get(falante),
            "texto": texto,
        })

    dados = {
        "status": "transcrição automática pendente de conferência",
        "arquivo": args.midia.name,
        "sha256": sha256,
        "duracao": timestamp(len(audio) / 16000),
        "idioma": info.language,
        "modelo": args.modelo,
        "diarizacao": args.diarizacao.name if args.diarizacao else fonte,
        "falas": falas,
    }
    conteudo = json.dumps(dados, ensure_ascii=False, indent=2) + "\n"
    with args.saida.open("x", encoding="utf-8") as arquivo:
        arquivo.write(conteudo)


if __name__ == "__main__":
    main()
