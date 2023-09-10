# :dart: Teste de Software: Um Guia Prático em Casos 

Este guia de casos foi desenvolvido por meio da metodologia Aprendizagem Baseada em Casos, com o objetivo de ser acessível e também aplicável em disciplinas de Engenharia de Software
ou qualquer pessoa que esteja interessada, independentemente do seu nível de experiência. À medida que você avança, encontrará não apenas teoria, mas também orientações práticas e 
exemplos mais próximos do real que o ajudarão a aprimorar suas habilidades de teste de software.

## :bulb: Como a Aprendizagem Baseada em Casos pode contribuir no ensino em teste de software?

A Aprendizagem Baseada em Casos é uma estratégia ativa que utiliza estudo de casos envolvendo o aluno no ambiente de aprendizagem, tornando-o protagonista daquele cenário, 
proporcionando ao mesmo uma experiência cada vez mais significativa dentro da sala de aula.

O que é um caso?

Caso é uma estória real ou fictícia, documentada, que envolve:

  - situação problema;
  - contexto;
  - personagens;

## :trophy: E o teste de software, por que ele é tão importante?

Martin Fowler, em seu livro Refatoração, afirma que:

>  [...] Se você observar como a maioria dos programadores gasta o tempo, verá que escrever código, na verdade, representa uma pequena fração desse tempo.
> Uma parte é gasta para descobrir o que está acontecendo, outra, no design, mais a maior parte do tempo é gasta com depuração [...]

Essa reflexão que Martin faz pensarmos qual atenção estamos dando ao teste de software.
Será que vale a pena realizar entregas rápidas, quando temos que gastar vários dias de depuração procurando por bugs?

O Ciclo de Vida de Desenvolvimento de Software (SDLC) contempla todo o processo para entrega de um produto, geralmente constituído pelas etapas de
planejamento, modelagem, construção e aprimoramento. 

O teste de software não é apenas uma etapa final do ciclo de desenvolvimento e sim uma disciplina que permeia todo o processo, garantindo que você entregue 
software de alta qualidade que atenda às expectativas dos seus usuários. 

## Roteiro 

1. [Técnicas de Teste](#tecnicateste)
2. [Critérios de Teste](#criterioteste)
    - Exemplos de critérios para o Teste Funcional;
    - Exemplos de critérios para Teste Estrutural;
4. [Another paragraph](#paragraph2)

### Técnicas de Teste <a name="tecnicateste"></a>
Como é inviável testar todos cenários possíveis pela quantidade infinita de combinações, utilizamos heurísticas(técnicas) de teste que são guias de como se projetar bons casos de testes.
As mais conhecidas são:

| Técnica de Teste | Objetivo                                                                                                                                                                         |
| :--:    | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  Teste caixa branca ou Teste Estrutural | Exige um conhecimento da estrutura interna, o design e a codificação do software são testados para verificar o fluxo de entrada-saída e melhorar o design, a usabilidade e a segurança. No teste de caixa branca, o código é visível para os testadores, por isso também é chamado de teste de caixa clara, teste de caixa aberta, teste de caixa transparente, teste baseado em código e teste de caixa de vidro.                                 |
|  Teste caixa cinza   | Exige um conhecimento parcial da estrutura interna do aplicativo. O objetivo do teste de caixa cinza é pesquisar e identificar os defeitos devido à estrutura inadequada do código ou uso inadequado dos aplicativos. |
|  Teste caixa preta / Teste Funcional / Baseado em Especificação  | Não se exige um conhecimento do funcionamenrto interno do software, o objetivo é verificar se o comportamento da funcionalidade está ocorrendo de acordo com o esperado na especificação  |

As técnicas de teste utilizam os chamados "Critérios de Teste" para definir o que é importante de ser testado, evitando assim redundância de testes.

### Critérios de Teste <a name="criterioteste"></a>

De modo geral, um critério de teste se preocupa em resposder as seguintes perguntas:

- Como slecionar valores de entrada para criar bons casos de teste?
- Quantos casos de teste devem ser criados?
- Quando parar de testar?

| Critério | Objetivo                                                                                                                                                                         |
| :--:    | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  Teste caixa branca ou Teste Estrutural |     Baseados na Complexidade, Baseados em Fluxo de Controle e Baseados em Fluxo de Dados          |
|  Teste caixa cinza   | |
|  Teste caixa preta / Teste Funcional / Baseado em Especificação  |  Particionamento em Classes de Equivalência, Análise do Valor Limite e Grafo Causa-Efeito |



  









Referências:
https://roadmap.sh/qa
https://www.guru99.com/v-model-software-testing.html
https://www.iso.org/obp/ui/en/#iso:std:iso-iec-ieee:29119:-3:ed-2:v1:en
https://softdesign.com.br/blog/a-importancia-do-teste-de-software/
