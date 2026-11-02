# Formatos e entregas

Resumo: regras e o que entregar por formato, e uso dos templates de arte. Entregue só o nível
de detalhe pedido. Sumário: Reel → Carrossel → Stories → Post estático → Calendário →
Impulsionado → Legenda/SEO → Templates de arte.

Regra de ouro do escopo: se pediram só a legenda, entregue a legenda. As listas completas
abaixo são o teto de uma entrega, não o piso de toda resposta.

## Reels

Padrão: 15 a 35 segundos, vertical 9:16. Gancho em 0 a 2s. Contexto 2 a 7s. Explicação principal
direta. Consequência ou cuidado prático. Fechamento informativo. CTA neutro. Mudança visual
(enquadramento, texto, card, B-roll) a cada 1,5 a 3s quando melhorar retenção. Legenda dinâmica
mas legível, dentro da zona segura. Primeira imagem compreensível sem áudio. Não depender de
dancinha, humor forçado ou áudio viral incompatível com a marca.

Roteiro completo (só quando pedirem "roteiro completo"): 1) objetivo; 2) público; 3) estágio de
consciência; 4) duração; 5) cinco opções de gancho; 6) roteiro final com marcações de tempo;
7) texto falado; 8) texto na tela; 9) enquadramento; 10) cortes e B-roll; 11) título de capa até
oito palavras; 12) legenda; 13) CTA; 14) três a cinco hashtags específicas; 15) duas variações
A/B; 16) fontes jurídicas para conferência interna; 17) checklist ético.
Se pediram só o texto falado, entregue só o texto falado.

## Carrossel

Direção de arte, processo e autoavaliação de carrossel são regidos por
`direcao-de-arte-e-carrossel.md`, com o `../../../references/modelos-locais.md` (6 direções de arte + 9
layouts de slide). O resumo abaixo continua valendo como piso editorial e de escopo.

Padrão: 6 a 9 slides. Capa com tensão informativa, não clickbait. Um único ponto por slide.
Progressão lógica. Pouco texto. Exemplos práticos. Um slide de consequência ou cuidado.
Fechamento útil. CTA neutro. Coerência com preto, marfim, branco e dourado. Imagens escuras e
editoriais quando necessárias, nunca prejudicando a leitura. Evitar todos os slides com a mesma
composição.

Entrega completa: 1) três títulos de capa; 2) objetivo e público; 3) texto slide a slide;
4) hierarquia visual; 5) sugestão de imagem ou elemento por slide; 6) orientação de contraste;
7) legenda; 8) CTA; 9) texto alternativo de acessibilidade; 10) fontes jurídicas; 11) checklist ético.

## Stories

Sequência de 3 a 5 telas: identificação; pergunta ou contexto; informação; interação;
fechamento. Enquete, quiz ou caixa de perguntas só quando houver pergunta específica. Não
oferecer consultoria individual gratuita pela caixa de perguntas; responder de forma geral e
educativa.

## Post estático

Entregar: título curto; subtítulo opcional; ideia visual; legenda; CTA; fonte jurídica interna;
checklist ético.

## Calendário editorial

Equilibrar áreas, formatos e estágios de consciência. Evitar duas publicações seguidas com a
mesma promessa narrativa. Para cada item: objetivo, público, formato, gancho, pilar, área e
métrica principal. Considerar capacidade real de produção. Propor reaproveitamento entre Reel,
carrossel e Stories. Não encher de datas comemorativas irrelevantes. Conteúdo local só com
função editorial. Detalhes de estratégia em `estrategia-editorial-e-conversao.md`.

## Conteúdo impulsionado

Separar do orgânico. O impulsionado deve ser ainda mais informativo e sóbrio. Sem oferta de
serviço, preço, gratuidade, promessa, urgência comercial, chamada para contratação ou
segmentação oportunista de pessoas vulneráveis.

## Legenda e SEO social

Estrutura: 1) primeira linha que complementa o gancho; 2) contexto curto; 3) explicação útil;
4) consequência prática; 5) cautela jurídica quando necessária; 6) CTA neutro.
Regras: não repetir o vídeo inteiro; não começar toda legenda com pergunta; inserir termos que o
público pesquisaria; citar Araucária, Curitiba ou Paraná só quando relevante; três a cinco
hashtags específicas; evitar #direito, #advogado, #justiça quando não ajudam a descoberta; não
usar dezenas de hashtags; emoji no máximo um, funcional; sem blocos intermináveis.

## Templates de arte (assets)

Em `assets/` estão a logo do escritório (branca para fundo escuro, dourada para fundo claro) e
dois templates HTML self-contained com a identidade já aplicada:
- `../../../references/modelos-locais.md` — studio principal de carrossel: 6 direções de arte (premium,
  editorial, cinema, minimal, corporate, humano) e 9 layouts de slide (capa, gancho, número,
  comparação, lista, citação, passo, destaque, cta). Escolha `STYLE`, monte o array `slides`
  variando o layout de cada um, exporte cada `#slide-N` em PNG. `?demo=1` mostra as 6 direções.
  Regido por `direcao-de-arte-e-carrossel.md`. Use este como padrão para carrossel.
- `../../../references/modelos-locais.md` — versão antiga, fundo sólido, uma composição só. Mantido para
  peças simples; para carrossel novo prefira o studio.
- `../../../references/modelos-locais.md` — mesma linha, mas compõe o texto SOBRE uma foto por slide, com degradê escuro que garante leitura sem apagar a imagem. Ideal para série editorial com fotos (motoboy, escritório, fórum). Edite o array de slides no topo (badge, título com `<span class="g">`, subtítulo, caminho da foto e posição) e exporte cada `#slide-N` em PNG. Foto ideal 1080x1350 (4:5), que serve para Instagram e Threads.
- `../../../references/modelos-locais.md` — gera thumbnail de YouTube (1280x720) e capa de Reels (1080x1350).
Edite o bloco de configuração no topo (cores, @ e texto de cada slide) e exporte cada peça em
PNG (abrindo no navegador ou renderizando em modo headless). A paleta padrão já é o dourado
#dd9a37 sobre grafite. Mantenha o dourado como acento, conforme `marca-e-posicionamento.md`.
