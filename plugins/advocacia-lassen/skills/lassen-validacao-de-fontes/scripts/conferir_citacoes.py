"""Confere citações marcadas em uma minuta Markdown e gera texto sem as marcas."""

import argparse
import json
import re
from datetime import date
from pathlib import Path
from urllib.parse import urlsplit

BLOCO = re.compile(r"^:::fonte ([A-Z][A-Z0-9-]*)\n(.+?)\n:::[ \t]*$", re.M | re.S)
INDICIO = re.compile(
    r":::|https?://|\b(?:arts?\.?\s*\d+|artigos?\s+\d+|§\s*\d+|"
    r"leis?\s+(?:n[.º°o]*\s*)?\d|ac[oó]rdãos?|jurisprud[eê]ncia|"
    r"precedentes?|s[uú]mulas?|tema\s+\d+|REsp|AREsp|RE|ARE|ADI|ADPF|"
    r"IRDR|IAC|CPC|CLT|STF|STJ|TST|C[oó]digo\s+(?:Civil|Penal|de Processo))\b|"
    r"\b\d{7}-\d{2}\.\d{4}\.\d\.\d{2}\.\d{4}\b",
    re.I,
)
CAMPOS = ("identificacao", "localizador", "situacao", "aderencia", "texto_aprovado")


def validar_fonte(fonte, texto, hoje):
    if not isinstance(fonte, dict) or fonte.get("status") != "apta":
        return "fonte ausente ou sem status apta"
    if any(not isinstance(fonte.get(campo), str) or not fonte[campo].strip()
           for campo in CAMPOS):
        return "registro de verificação incompleto"
    try:
        url = urlsplit(fonte["url_oficial"])
        host = url.hostname or ""
        consulta = date.fromisoformat(fonte["consultada_em"])
    except (KeyError, ValueError, TypeError, AttributeError):
        return "URL oficial ou data inválida"
    if (url.scheme != "https" or url.username or url.password or not url.path.strip("/")
            or not host.endswith((".gov.br", ".jus.br", ".leg.br", ".mp.br", ".def.br"))):
        return "URL sem página específica em domínio institucional brasileiro"
    if consulta > hoje:
        return "data de consulta posterior à conferência"
    if fonte["texto_aprovado"].strip() != texto:
        return "trecho diferente do texto aprovado"
    return None


def conferir(minuta, registro, hoje):
    erros = []
    partes = []
    cursor = 0

    def conferir_texto(inicio, fim):
        texto = minuta[inicio:fim]
        for indicio in INDICIO.finditer(texto):
            linha = minuta.count("\n", 0, inicio + indicio.start()) + 1
            erros.append(f"linha {linha}: possível citação fora de bloco ({indicio.group()})")
        if re.search(r"\b(?:art(?:igo)?s?)\s*\.\s*\d", texto, re.I):
            erros.append("referência a dispositivo fora de bloco")
        partes.append(texto)

    for bloco in BLOCO.finditer(minuta):
        conferir_texto(cursor, bloco.start())
        identificador, texto = bloco.groups()
        texto = texto.strip()
        erro = validar_fonte(registro.get(identificador), texto, hoje)
        if any(linha.lstrip().startswith(":::") for linha in texto.splitlines()):
            erro = "marca de fonte aninhada ou inválida"
        if erro:
            linha = minuta.count("\n", 0, bloco.start()) + 1
            erros.append(f"linha {linha}, {identificador}: {erro}")
        partes.append(texto)
        cursor = bloco.end()

    conferir_texto(cursor, len(minuta))
    return erros, "".join(partes)


def registro_sem_duplicatas(pares):
    registro = {}
    for chave, valor in pares:
        if chave in registro:
            raise ValueError(f"Chave duplicada no registro: {chave}")
        registro[chave] = valor
    return registro


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("minuta", type=Path)
    parser.add_argument("registro", type=Path)
    parser.add_argument("saida", type=Path, help="Novo arquivo Markdown de saída")
    parser.add_argument("--data", required=True, type=date.fromisoformat)
    args = parser.parse_args()
    try:
        minuta = args.minuta.read_text(encoding="utf-8-sig")
        registro = json.loads(
            args.registro.read_text(encoding="utf-8-sig"),
            object_pairs_hook=registro_sem_duplicatas,
        )
        if not minuta.strip() or not isinstance(registro, dict):
            raise ValueError("Minuta vazia ou registro fora do formato.")
        erros, resultado = conferir(minuta, registro, args.data)
        if erros:
            parser.exit(1, "Conferência bloqueada:\n" + "\n".join(erros) + "\n")
        with args.saida.open("x", encoding="utf-8") as arquivo:
            arquivo.write(resultado)
    except (OSError, ValueError) as erro:
        parser.exit(2, f"Falha na conferência: {erro}\n")
    print("Conferência técnica concluída. Saída criada.")


if __name__ == "__main__":
    main()
