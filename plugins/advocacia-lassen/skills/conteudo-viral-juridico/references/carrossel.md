# Carrossel (Instagram e LinkedIn)

O carrossel é o formato que mais gera salvamento no jurídico, porque ensina passo a passo e
a pessoa guarda pra depois. Ele vive de duas coisas: a capa (que ganha o clique) e o ritmo
(cada slide tem que empurrar pro próximo).

## Estrutura slide a slide

O padrão que funciona tem de 6 a 9 slides. Menos que 6 raramente entrega valor de salvar;
mais que 10 cansa.

**Slide 1 (capa) — o gancho.** É o mais importante, é o que decide tudo. Só o gancho, em
texto grande, e um micro-indício de que tem mais ("arrasta"). Nada de introdução. Ex.:
"3 erros que fazem você perder a rescisão trabalhista".

**Slide 2 — a tensão / por que importa.** Aprofunda a dor ou a stakes. Faz a pessoa sentir
que precisa saber. "A maioria descobre tarde demais, quando o prazo já passou."

**Slides 3 a N-1 — o conteúdo, um ponto por slide.** Aqui está o valor. Cada slide entrega
UMA ideia: um erro, um passo, um documento, uma regra. Título curto no topo do slide +
explicação enxuta. Um ponto por slide é o que dá ritmo e o que faz salvar. Não empilhe dois
pontos num slide só.

**Slide N-1 (penúltimo) — recapitulação ou virada.** Resume os pontos ou dá o insight que
amarra tudo. "Junta esses três documentos desde o primeiro dia e você nunca fica na mão."

**Slide N (último) — CTA leve.** Salvar, compartilhar ou comentar. Dentro da OAB, sem
promessa e sem captação. "Salva pra quando precisar" ou "Manda pra alguém que tá passando
por isso". Pode ter o @ do perfil e um convite a seguir.

## Ritmo de leitura

- **Uma ideia por slide.** Repetindo porque é o erro nº 1: slide lotado mata o ritmo.
- **Frase curta.** Carrossel não é artigo. Cada slide se lê em 2 a 4 segundos.
- **Continuidade.** Termine slides com gancho pro próximo quando der ("e o segundo é pior").
- **Número no canto** (1/7, 2/7...) ajuda a pessoa a saber onde está e incentiva terminar.

## Design (aplicar o sistema de design-visual.md)

- Todos os slides com a mesma paleta, mesma fonte, mesma margem, mesma posição do @.
- Capa com contraste mais alto (é a que compete no feed).
- Muito respiro. Margem generosa. Texto nunca colado na borda (deixe zona segura de ~80px,
  porque o Instagram corta as beiradas na prévia).
- Cor de acento só na palavra que importa de cada slide.
- Assinatura discreta (@ do perfil) no mesmo canto em todos.

## Tamanho e exportação

- **Instagram:** 1080 x 1350 px (retrato 4:5, ocupa mais tela) é o ideal. 1080 x 1080
  (quadrado) se o usuário preferir.
- **LinkedIn:** costuma ser PDF ou 1080 x 1080. Tom mais analítico, menos "dor de feed".

Para gerar as imagens, use `../../../references/modelos-locais.md`. Preencha o bloco de
configuração no topo do arquivo com: a paleta (cor de marca, neutro escuro, neutro claro,
acento), as fontes, o @ do perfil e o conteúdo de cada slide (título + corpo + tipo de
slide: capa, conteúdo ou CTA). Depois:

1. Se houver navegador/Playwright neste ambiente: abra o HTML, renderize cada slide no
   tamanho definido e exporte como PNG. Entregue os PNGs pro usuário.
2. Se não houver: entregue o HTML preenchido e explique que basta abrir no navegador; cada
   slide já está no tamanho certo pra dar print ou usar a função de exportar.

O template já cuida de margens seguras, hierarquia e numeração. Seu trabalho é o conteúdo e
as cores, não reinventar o layout.
