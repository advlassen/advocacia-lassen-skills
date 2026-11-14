"""Exercita a CLI com uma emenda à inicial inteiramente fictícia."""

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "conferir_citacoes.py"
DATA = "2026-11-14"
TEXTO = "Em cumprimento ao despacho de emenda, a autora discrimina os pedidos, conforme os arts. 319, IV, e 321 do CPC."
FONTE = {
    "status": "apta",
    "identificacao": "Lei 13.105/2015, arts. 319, IV, e 321, caput",
    "url_oficial": "https://www2.camara.leg.br/legin/fed/lei/2015/lei-13105-16-marco-2015-780273-normaatualizada-pl.html",
    "consultada_em": DATA,
    "localizador": "Capítulo II, Seção I, arts. 319, IV, e 321, caput",
    "situacao": "Redação consultada no texto atualizado da Câmara",
    "aderencia": "Emenda à inicial cível para especificar pedidos por determinação judicial",
    "texto_aprovado": TEXTO,
}
INICIO = "# Emenda à petição inicial\n\nAo Juízo Cível da Comarca Alfa\n\nParte Autora A, nos autos em face de Parte Ré B, apresenta emenda.\n\n"
FIM = "\n\nA autora pede a devolução dos R$ 800,00 pagos pelo serviço descrito no comprovante anexo e o recebimento desta emenda.\n"
BLOCO = f":::fonte CPC\n{TEXTO}\n:::"


class Conferencia(unittest.TestCase):
    def executar(self, minuta, registro, codigo):
        with tempfile.TemporaryDirectory() as pasta:
            raiz = Path(pasta)
            entrada, memoria, saida = [raiz / nome for nome in ("minuta.md", "fontes.json", "final.md")]
            entrada.write_text(minuta, encoding="utf-8")
            memoria.write_text(registro if isinstance(registro, str) else json.dumps(registro), encoding="utf-8")
            retorno = subprocess.run(
                [sys.executable, str(SCRIPT), str(entrada), str(memoria), str(saida), "--data", DATA],
                capture_output=True,
            )
            self.assertEqual(retorno.returncode, codigo, retorno.stderr)
            self.assertEqual(saida.exists(), codigo == 0)
            if codigo == 0:
                self.assertEqual(saida.read_text(encoding="utf-8"), INICIO + TEXTO + FIM)

    def test_minuta_corrigida(self):
        self.executar(INICIO + BLOCO + FIM, {"CPC": FONTE}, 0)

    def test_minuta_com_referencia_sem_fonte(self):
        self.executar(INICIO + BLOCO + "\n\nREsp [identificador fictício]." + FIM, {"CPC": FONTE}, 1)

    def test_fonte_marcada_sem_registro(self):
        self.executar(INICIO + BLOCO + FIM, {}, 1)

    def test_fonte_reprovada_ou_incompleta(self):
        for campos in ({"status": "não verificada"}, {"localizador": ""},
                      {"url_oficial": "https://externo.example/documento"},
                      {"consultada_em": "2026-11-15"}):
            with self.subTest(campos=campos):
                self.executar(INICIO + BLOCO + FIM, {"CPC": FONTE | campos}, 1)

    def test_registro_com_chave_duplicada(self):
        fonte = json.dumps(FONTE)
        registro = '{"CPC": {"status": "não verificada"}, "CPC": ' + fonte + '}'
        self.executar(INICIO + BLOCO + FIM, registro, 2)

    def test_texto_alterado_depois_da_validacao(self):
        self.executar(INICIO + BLOCO.replace("321", "322") + FIM, {"CPC": FONTE}, 1)


if __name__ == "__main__":
    unittest.main()
