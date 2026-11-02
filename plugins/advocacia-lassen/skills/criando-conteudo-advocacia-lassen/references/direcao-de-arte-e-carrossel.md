# Direção de arte e carrossel

Como a Advocacia Lassen faz carrossel de nível agência: nunca genérico, nunca com cara de
template, acabamento fora do Canva. Esta referência manda em todo carrossel.

Ferramenta: `../../../references/modelos-locais.md`. Um arquivo, paleta oficial única (preto, marfim,
branco e dourado), dois tons (claro e escuro) e uma biblioteca de layouts de slide com os
elementos novos: capa dividida com foto, quiz, mito x fato, bloco de regra, grade de cartões,
fluxo com setas, checklist em painel, e fechamento. Cabeçalho, rodapé e barra de progresso
entram sozinhos. A logo real da marca já vem embutida: dourada nos fundos claros, branca nos
escuros. Cada `#slide-N` sai 1080x1350 (feed 4:5).

## Regra que rege tudo
Cor é padrão fixo, não se inventa. Toda peça usa a identidade única: preto profundo, marfim,
branco e o dourado da marca (#dd9a37). O que varia de um carrossel pro outro é o tom de cada
slide (claro ou escuro), o layout usado e a composição, nunca a paleta. Antes de fechar, o teste:
"parece escritório jurídico comum ou marca jurídica premium?". Se comum, refaz.

Banir da capa e dos ganchos: "Você sabia?", "Confira seus direitos", "Procure um advogado",
"Entenda a lei". São o oposto de diferenciação. Buscar curiosidade, identificação, dor,
consequência, solução, autoridade.

## Paleta, tom e tipografia
- Paleta oficial única: preto profundo, marfim, branco, dourado #dd9a37. No máximo três cores
  dominantes por slide. O dourado é acento: destaca a palavra que importa, um número, um traço,
  a assinatura. Não vira preenchimento de fundo inteiro (a exceção é um cartão de "realidade" ou
  um selo pontual em dourado, usado com parcimônia).
- Dois tons por slide, no campo `tone`: `light` (fundo marfim, texto escuro) e `dark` (fundo
  quase preto, texto marfim). Alterne os tons ao longo do carrossel pra o feed não ficar
  monocromático; capa e fechamento costumam ser claros, os slides de peso jurídico ficam bem no
  escuro.
- Logo automática: dourada no tom claro, branca no tom escuro. Nada a fazer, o studio troca
  sozinho.
- Tipografia: títulos em Sora (sans geométrica, forte, legível no celular), corpo em Inter,
  monograma da logo em serifada. Uma palavra do título em dourado (marque com `<em>` ou
  `<span class="n">`) puxa o olho pro ponto certo.

## Processo (nesta ordem, sempre antes de desenhar)
1. Objetivo: autoridade, educação, conversão, relacionamento, alerta, quebra de mito,
   atualização jurídica ou storytelling. Um só por peça.
2. Público: quem é, qual problema vive, qual medo tem, qual decisão precisa tomar.
3. Ideia central em forma de tensão. Não "responsabilidade do sócio"; e sim "quando a dívida da
   empresa pode chegar ao patrimônio pessoal do dono?".
4. Roteiro slide a slide, escolhendo o `tone` e o `layout` de cada um e variando ambos.
5. Copy nos frameworks abaixo.
6. Legenda (não repete o carrossel).
7. Autoavaliação com notas. Nota < 9 em qualquer eixo, refaz.

## Biblioteca de layouts (campo `layout` de cada slide)
- **cover** — capa dividida: painel de texto à esquerda (eyebrow, título curto de alto impacto
  com uma palavra em dourado, subtítulo, botão "arraste") e painel vertical de foto à direita,
  com um rótulo no topo e um cartão flutuante de reforço. Gere 3 conceitos de capa e escolha o
  melhor. Fraco: "Direito empresarial". Forte: "Seu CNPJ não é um escudo automático".
- **quiz** — teste rápido: 2 a 4 perguntas em cartões numerados com pílula "SIM / NÃO" e uma
  faixa de conclusão. Ótimo pro segundo slide, faz a pessoa se reconhecer.
- **mitofato** — mito x realidade em dois cartões empilhados: o mito num cartão neutro com ✕, a
  realidade num cartão preenchido de dourado com ✓. É o coração da quebra de mito.
- **regra** — bloco de destaque grande (ex.: EMPRESA ≠ SÓCIO, ou DESVIO + CONFUSÃO) mais um
  cartão de artigo com o número da lei em chip. Usado pra fixar a regra ou a exceção jurídica.
- **grid** — grade de 3 a 4 cartões numerados, uma ideia por cartão, leitura rápida (sinais,
  tipos, erros).
- **fluxo** — passo a passo em cartões com setas entre eles, um cartão em destaque escuro, mais
  um box "Importante". Mostra uma sequência ou uma consequência em etapas.
- **check** — checklist em painel: itens com círculo de ✓, título e descrição, número à direita
  e fios finos separando. Usado pra "o que fazer".
- **close** — fechamento dividido, espelho da capa: título de conclusão, botão de CTA ético em
  dourado, aviso informativo e painel de foto. Sem "salve o post".

Padrão: 6 a 9 slides. Capa, um gancho/quiz, intermediários **de layouts diferentes**, fechamento.
Regra inegociável: **nunca dois slides seguidos com o mesmo layout**, e nunca um carrossel
inteiro só de "título + texto". Cada slide intermediário tem uma ideia, hierarquia própria e um
elemento visual próprio. Cabeçalho (logo + rótulo da seção), rodapé (@perfil + número) e barra
de progresso aparecem sozinhos nos slides de conteúdo.

## Copywriting
Nunca escrever como petição. "O art. 50 do CC autoriza a desconsideração" vira "quando há abuso,
o juiz pode alcançar os bens do sócio". Ferramentas: AIDA, PAS, storytelling, gatilho de
autoridade, curiosidade. Fio condutor do carrossel inteiro:
Problema → Consequência → Explicação → Solução → Ação.

## Legenda (segunda etapa, não repete o carrossel)
1. Primeira frase que prende sozinha. 2. Desenvolvimento em narrativa (situação, problema,
consequência, reflexão; conversa estratégica, não artigo). 3. Explicação jurídica acessível
(o quê, por quê, qual cuidado). 4. Autoridade da marca inserida com naturalidade. 5. CTA final
variado e ético (compartilhar com quem precisa, enviar pra um sócio, acompanhar o perfil,
responder uma dúvida). Hashtags específicas e poucas.

## Entrega final obrigatória
1. Estratégia: objetivo, público, dor, conceito.
2. Direção de arte: tons usados por slide e por quê, e como a paleta e a logo se aplicam.
3. Roteiro slide a slide: título, texto, imagem sugerida (para cover/close), o `tone` e o
   `layout` do studio usados.
4. Legenda completa (gancho, desenvolvimento, autoridade, CTA) + hashtags.
5. Avaliação, notas 0-10: Design, Originalidade, Retenção, Autoridade jurídica, Potencial de
   conversão. **Qualquer nota < 9 = refazer** aquele ponto antes de entregar.

## OAB antes de tudo
Roda o filtro de `etica-oab.md` na copy e na legenda: sem promessa de resultado, captação,
honorário, superlativo, sensacionalismo ou mercantilização. Direção premium não afrouxa a
ética; sobriedade é parte do posicionamento.

## Como usar o studio (`../../../references/modelos-locais.md`)
1. Abra o arquivo. Cada slide é um objeto no array `slides`, no fim do `<script>`.
2. Em cada objeto defina `tone` ("light" ou "dark") e `layout` (cover | quiz | mitofato | regra
   | grid | fluxo | check | close) e preencha os campos daquele layout. Use `<em>` ou
   `<span class="n">` pra pintar uma palavra no dourado.
3. Nos layouts com foto (cover e close), aponte `foto:` para o caminho da sua imagem vertical
   (ex.: `foto:'img/capa.png'`). Use foto escura, com respiro à esquerda; nada de banco de imagem
   genérico. Deixe `foto:''` se ainda não tiver a arte.
4. Abra no navegador. Cada `#slide-N` é 1080x1350. Exporte em PNG (print enquadrado ou render
   headless) e, pra postar, converta para JPG de alta qualidade.
5. A logo real da marca já vem embutida em base64 (dourada nos tons claros, branca nos escuros).
   Nada a fazer.
