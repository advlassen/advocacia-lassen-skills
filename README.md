<p align="center"><img src="plugins/advocacia-lassen/assets/logo-lassen-completa-preta-transparente.png" alt="Advocacia Lassen" width="360"></p>

# Skills da Advocacia Lassen

Acervo público com 27 skills para trabalho jurídico, pesquisa acadêmica, documentos, gestão e comunicação. Exportação da versão 1.4.0, preparada para Claude Code, com as instruções e os logotipos do escritório.

O pacote orienta o trabalho e não fornece acesso a tribunais, CRM, áudio, Word ou serviços externos. Os recursos efetivos dependem do ambiente. Nenhuma skill assina, protocola, compartilha ou contata terceiros por conta própria.

## Usar localmente sem instalar

Com Claude Code já instalado e autenticado, abra um terminal na raiz deste repositório:

```sh
claude --plugin-dir ./plugins/advocacia-lassen
```

Na sessão, invoque por exemplo:

```text
/advocacia-lassen:sistema-juridico-lassen
/advocacia-lassen:lassen-depoimentos-transcricoes
/advocacia-lassen:lassen-pesquisa-academica
/advocacia-lassen:lassen-redacao-de-pecas
```

O argumento aponta para o diretório do plugin. A raiz deste repositório é o marketplace. A organização e o prefixo dos comandos seguem a [documentação de criação de plugins](https://code.claude.com/docs/en/plugins/create).

## Instalar pelo marketplace do GitHub

O catálogo é público. O Claude Code usa a autenticação configurada no ambiente. Mantenha credenciais e arquivos de casos fora do repositório.

Execute no terminal, se desejar instalar:

```sh
claude plugin marketplace add advlassen/advocacia-lassen-skills
claude plugin install advocacia-lassen@advocacia-lassen-skills
```

Alternativa a partir de uma cópia local:

```sh
claude plugin marketplace add .
claude plugin install advocacia-lassen@advocacia-lassen-skills
```

As etapas de catálogo e instalação são descritas na [documentação oficial de marketplaces](https://code.claude.com/docs/en/plugin-marketplaces). A entrada usa uma origem relativa ao repositório conforme a [referência de marketplaces](https://code.claude.com/docs/en/plugins/marketplace-reference).

## Validar fontes para petição ou parecer

Use [lassen-validacao-de-fontes](plugins/advocacia-lassen/skills/lassen-validacao-de-fontes/SKILL.md) para decidir quais fontes oficiais sustentam a proposição e se aplicam ao caso.

## Organização

- `.claude-plugin/marketplace.json`: catálogo com um plugin.
- `plugins/advocacia-lassen/.claude-plugin/plugin.json`: identidade e versão do plugin.
- `plugins/advocacia-lassen/skills/`: 27 diretórios com `SKILL.md` e referências próprias.
- `plugins/advocacia-lassen/references/`: regras comuns, fluxo auditável e guia de modelos locais.
- `plugins/advocacia-lassen/assets/`: logotipos; a logo completa oficial é `logo-lassen-completa-preta-transparente.png` (preto puro, fundo transparente).

As skills usam nome e descrição no frontmatter e mantêm os arquivos de apoio dentro do plugin. Consulte a [documentação oficial de skills](https://code.claude.com/docs/en/skills).

## Modelos e privacidade

Os sete DOCX privados e os cinco HTML internos não acompanham esta exportação. Os DOCX têm dados profissionais, contatos ou metadados pessoais; o exemplar de petição também contém narrativa demonstrativa. Os HTML incluem scripts, imagens embutidas e fontes externas sem documentação de licença suficiente para redistribuição. Não foram alterados no plugin privado.

Para produzir documentos com fidelidade visual, disponibilize o modelo apropriado separadamente em ambiente autorizado. Leia o [guia de modelos locais](plugins/advocacia-lassen/references/modelos-locais.md). Não adicione documentos preenchidos, autos, dados de clientes, credenciais ou backups a este repositório.

## Conferência e limites

A preparação conferiu JSON, frontmatter, nomes das 26 skills, referências internas, presença dos logotipos e remoção dos identificadores conhecidos. Não equivale a auditoria jurídica de todos os temas nem à execução das skills no Claude Code. Nenhum áudio foi processado e nenhum motor de transcrição foi instalado.

Para conferir o pacote com seu Claude Code, sem instalar o plugin:

```sh
claude plugin validate .
claude plugin validate ./plugins/advocacia-lassen
```

Esses comandos são instruções para o usuário; não foram executados nesta preparação. Versões antigas do Claude Code podem exigir atualização segundo a documentação do fornecedor.

## Direitos e acesso

O GitHub disponibiliza o repositório para consulta pública. Não há concessão de licença open-source, autorização geral de redistribuição nem licença de uso da marca. Consulte [direitos e proveniência](NOTICE.md) e [origem da exportação](PROVENANCE.md). Adicionar colaboradores, tornar público ou escolher licença exige decisão específica do responsável.


## Atualização 1.3.1

A logo preta completa usa fundo branco puro #FFFFFF, opaco. A limpeza foi determinística, sem redesenhar: desenho, tipografia e vizinhança de antialiasing preservados. As variantes branca e dourada mantêm transparência para os usos adequados. O README utiliza a variante preta completa.

O [checklist de fontes brasileiras](plugins/advocacia-lassen/references/checklist-fontes-brasileiras.md) reforça a verificação de legislação e jurisprudência por tarefa. Não é um catálogo de precedentes, monitoramento automático ou garantia de atualização permanente.

## Atualização 1.4.0

A skill lassen-atualizacao-juridica revalida, por tarefa, leis e precedentes de uma pesquisa anterior ou inicial, com quadro mudou/permanece/não confirmado, impacto e fontes. Ela não monitora sozinha, agenda pesquisas nem declara atualização sem acesso atual suficiente.

## 1.4.2 — correção delimitada
Removida a inferência de mentira por excesso de justificativas na referência de audiências; usar conteúdo, contexto, percepção relatada e prova. As 26 skills e os assets neutros foram preservados. Esta exportação parte da 1.4.0 e recebe esta correção; não é cópia integral do plugin ChatGPT 1.4.2. A entrega DOCX + PDF padrão já configurada no Projeto Claude continua sendo uma regra expressa das instruções daquele Projeto, que prevalece sobre instruções antigas de formato desta exportação. Não houve sincronização automática de todas as alterações da versão ChatGPT 1.4.1. Permanecem as omissões de DOCX/HTML documentadas em EXPORT-REVIEW.md.
