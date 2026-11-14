# Transcrição local de audiências

O script [transcrever.py](../scripts/transcrever.py) recebe áudio ou vídeo e produz JSON com IDs de trechos, início e fim estimados, rótulos de falantes e SHA-256 da mídia. A inferência roda na máquina, em CPU. O download inicial de dependências e modelos exige internet.

## Executar

Instale [uv](https://docs.astral.sh/uv/getting-started/installation/). Para baixar o modelo de diarização pela primeira vez, aceite as condições do [Community-1](https://huggingface.co/pyannote/speaker-diarization-community-1) e disponibilize um token de leitura via variável de ambiente HF_TOKEN na sessão. Não inclua o token no comando, nos arquivos ou no histórico. O uv pode baixar Python 3.12.

Na raiz do repositório, com caminhos fora da árvore Git para mídia e resultado:

~~~powershell
uv run --python 3.12 plugins/advocacia-lassen/skills/lassen-depoimentos-transcricoes/scripts/transcrever.py "D:/Caso/audiencia.mp4" "D:/Caso/transcricao.json"
~~~

Para uso sem rede após provisionar dependências e modelos, use uv run --offline e forneça diretórios locais com --modelo e --diarizacao. Para mídia em outro idioma, ajuste --idioma. A decodificação usa a primeira faixa de áudio e carrega o áudio decodificado em memória. Se a gravação contiver faixas separadas ou exceder os recursos locais, confirme qual faixa examinar e documente o deslocamento de cada cópia de trabalho antes de citar horários.

O [faster-whisper](https://github.com/SYSTRAN/faster-whisper) estima os tempos das palavras. O Community-1 fornece turnos exclusivos para alinhar palavras com vozes. Falante nulo indica atribuição incerta. Os rótulos são locais ao arquivo e podem trocar entre gravações. Vozes simultâneas, omissões, nomes, números e negações exigem escuta dirigida.

## Da gravação à peça

1. Abra o original nos intervalos relevantes. Verifique o início da faixa, o contexto da pergunta e da resposta e eventuais retificações. Registre trechos inaudíveis ou sobrepostos após conferência.
2. Identifique pessoas ou papéis a partir de apresentação na gravação, ata ou outra evidência verificável. Registre a base e o intervalo que sustentam o vínculo. Mantenha rótulos genéricos quando a autoria continuar incerta.
3. Preserve o JSON bruto e registre as correções em cópia. Para cada passagem que for usada literalmente, anote o arquivo ou evento dos autos, ID, tempo inicial e final, falante, texto conferido e status da revisão.
4. Cruze a passagem com os demais elementos dos autos. Entregue a matriz com a ressalva ou retificação pertinente. Sinalize trechos pendentes de conferência para impedir que entrem como citações prontas.
