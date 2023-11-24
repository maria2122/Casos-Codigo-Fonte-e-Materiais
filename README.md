# :beetle: Sobre
> [!NOTE]
> [Apresentação do Trabalho](https://github.com/maria2122/teste-de-software-um-guia-pratico-em-casos/blob/main/SOBRE.md)   

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# :rocket: Um Repositório de Casos para Apoiar o Ensino em Teste de Software 

Este repositório de casos foi construído tendo como base os trabalhos “Casos em Administração”, (COSTA, 2023), que orientam sobre a construção de casos que podem ser utilizados no contexto da estratégia ativa Aprendizagem Baseada em Casos com o objetivo de serem aplicáveis em disciplinas de Engenharia de Software ou qualquer pessoa interessada, independentemente do seu nível de experiência. À medida que você avança, encontrará não apenas teoria, mas também orientações práticas e exemplos mais próximos do real que o ajudarão a aprimorar suas habilidades em teste de software.

## :bulb: Como a Aprendizagem Baseada em Casos pode contribuir no ensino em teste de software?

A Aprendizagem Baseada em Casos é uma estratégia ativa que utiliza casos envolvendo o aluno no ambiente de aprendizagem, tornando-o protagonista daquele cenário, 
proporcionando ao mesmo uma experiência cada vez mais significativa dentro da sala de aula.

O que é um caso?

Caso é uma estória real ou fictícia, documentada, que envolve:

  - situação problema;
  - contexto;
  - personagens;

## :trophy: E o teste de software, por que ele é tão importante?

Martin Fowler, em seu livro Refatoração, afirma que:

> [!NOTE]
>  [...]
 Se você observar como a maioria dos programadores gasta o tempo, verá que escrever código, na verdade, representa uma pequena fração desse tempo.
> Uma parte é gasta para descobrir o que está acontecendo, outra, no design, mais a maior parte do tempo é gasta com depuração [...]

Essa reflexão de Martin faz pensarmos sobre a atenção que estamos dando ao teste de software.
Será que vale a pena realizar entregas rápidas, quando temos que gastar vários dias de depuração procurando por bugs?

O Ciclo de Vida de Desenvolvimento de Software (SDLC) contempla todo o processo para entrega de um produto, geralmente constituído pelas etapas de
planejamento, modelagem, construção, implementação e aprimoramento. 

Dentro desse ciclo, o teste de software pode ser incorporado em todas as etapas do processo de desenvolvimento, e não é apenas a etapa final do ciclo de desenvolvimento, garantindo a entrega de um
software de alta qualidade que atenda às expectativas dos usuários. 

## :dart: Roteiro para Educadores: Como usar este repositório

Para revisar e contextualizar os aspectos centrais da área de Teste de Software, propomos o seguinte roteiro. Os itens 1 e 2 oferecem uma visão panorâmica das técnicas de teste (funcionais e estruturais) e critérios, enquanto os demais (itens 3, 4 e 5) fornecem recursos de apoio para educadores, incluindo roteiros e exemplos práticos de casos que podem ser trabalhados em sala.

1. [Técnicas de Teste](#tecnicateste)
2. [Critérios de Teste](#criterioteste)
3. [Roteiro para Aplicação de Teste Funcional](https://docs.google.com/document/d/1RdG_XKgvYdxRzPXjMMicgPi3h6lyFZfQrEsXTkSxU90/edit?usp=sharing)
4. [Roteiro para Aplicação de Teste Estrutural](https://docs.google.com/document/d/1h1yhhccpBc_vsN6PJtwXpkvEbNzr0d5lqRKhkVFoBZQ/edit?usp=sharing)
5. [Casos](#casos)

### 1. Técnicas de Teste <a name="tecnicateste"></a>
Como é inviável testar todos cenários possíveis pela quantidade infinita de combinações, utilizamos heurísticas(técnicas) de teste que são guias de como se projetar bons casos de testes.
As mais conhecidas são:

| Técnica de Teste | Objetivo                                                                                                                                                                         |
| :--:    | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  Teste caixa branca ou Teste Estrutural                          | Exige um conhecimento da estrutura interna, o design e a codificação do software são testados para verificar o fluxo de entrada-saída e melhorar o design, a usabilidade e a segurança. No teste de caixa branca, o código é visível para os testadores, por isso também é chamado de teste de caixa clara, teste de caixa aberta, teste de caixa transparente, **teste baseado em código** e teste de caixa de vidro.                                                                                                         |
|  Teste caixa preta / Teste Funcional / Baseado em Especificação  | Não se exige um conhecimento do funcionamenrto interno do software, o objetivo é verificar se o comportamento da funcionalidade está ocorrendo de acordo com o **esperado na especificação**                                                                                                                               |

As técnicas de teste utilizam os chamados "Critérios de Teste" para definir o que é importante de ser testado, evitando assim a redundância.

### 2. Critérios de Teste <a name="criterioteste"></a>

De modo geral, um critério de teste se preocupa em responder as seguintes perguntas:

- Como selecionar valores de entrada para criar bons casos de teste?
- Quantos casos de teste devem ser criados?
- Quando parar de testar?

| Critério | Objetivo                                                                                                                                                                        |
| :--:    | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  Teste Caixa Branca ou Teste Estrutural                          | Baseados na Complexidade, Baseados em Fluxo de Controle e Baseados em Fluxo de Dados          |
|  Teste Caixa Preta / Teste Funcional / Baseado em Especificação  |  Particionamento em Classes de Equivalência, Análise do Valor Limite e Grafo Causa-Efeito |

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<a name="casos"></a>

> [!WARNING]
> O que um CASO não é:
>
> - NÃO é apenas um CASO DE TESTE 
> - NÃO é apenas um EXEMPLO 
> - NÃO busca resposta CERTA X ERRADA 
> - NÃO recebe o conhecimento e sim CONSTRÓI o conhecimento

### 3. Casos 

Os casos foram categorizados em três níveis de complexidade (Iniciante, Intermediário e Avançado),   proporcionando a flexibilidade necessária para serem abordados e adaptados ao nível específico da turma em que estão sendo aplicados.

| Nível |   Perfil do Aluno                                                                                                                                                                    |
| :--:    | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------  |
|  1 - Iniciante     | Alunos que tenham conhecimento em lógica de programação, algoritmos e já tenham tido contato com as linguagens : HTML, CSS e JAVASCRIPT                                 |
|  2 - Intermediário | Alunos que tenham desenvolvido uma aplicação básica em qualquer linguagem atuando nas camadas BACKEND (Servidor de Aplicação, Persistência em Banco de Dados) e FRONTEND (Aplicação Cliente, Interfaces e Frameworks)|
|  3 - Avançado      | Alunos que tenham experiência acadêmica ou profissional em desenvolvimento de projetos nas camadas BACKEND e FRONTEND, bem como padrões de projetos, processos da Engenharia de Software(analise de requisitos, modelagem, construção e teste, manutenção) e controle de versão                                                                                                 |


#### :white_check_mark: Nível Iniciante

| Nome                                                                              | Descrição                                                  | Nível        |
| --------------------------------------------------------------------------------- | ---------------------------------------------------------- | ------------ |
| [ Funcional: Cadastro de Pacientes](https://docs.google.com/document/d/16G8MJRK_eI04Pz76TVssiHNcQ8nCVg-JTJ4ULjNOAHI/edit?usp=sharing)| Verifica Obrigatoriedade dos Campos do Formulário de Cadastro de Pacientes | 1-Inicitante |
| [ Funcional: Valida Visibilidade de Campos](https://docs.google.com/document/d/1N65molLxSZHBn3qbRDj6OBrOuvgQgZKyd3j0JEb32rE/edit?usp=sharing) | Valida Visibilidade de Campos                                     | 1-Inicitante |
| [ Funcional : Níveis e Acesso](https://docs.google.com/document/d/1R_epzkqvgcIB2qy1WMIhNc1emHQqjOxzcZIht8Wwsf0/edit?usp=sharing)| Valida Níveis de Acesso                                                         | 1-Inicitante |

#### :muscle: Nível Intermediário 

| Nome                                                                              | Descrição                                                  | Nível           |
| --------------------------------------------------------------------------------- | ---------------------------------------------------------- | ----------------|
| [Estrutural: Método Desconto](https://docs.google.com/document/d/1DM-ARr2XJHJJxnhRJLf6E-IQNsJ6cULhWZ16RvcJyuQ/edit?usp=sharing)| Valida Método de Desconto                                  | 2-Intermediário |
| [Estrutural: Calculadora](https://docs.google.com/document/d/1f22kWutXxun3H2AXPMs8dV_WTfJ4U80W9syCYIcRHg4/edit?usp=sharing)| Fluxo de controle de uma Calculadora                       | 2-Intermediário |

#### :cold_sweat: Nível Avançado 

| Nome                                                                              | Descrição                                                  | Nível      |
| --------------------------------------------------------------------------------- | ---------------------------------------------------------- | -----------|
| [Funcional: Módulos Financeiro e Contabilidade](https://docs.google.com/document/d/1LlkfZJ-MxYhFwL16d_F1nzF5ZQ6YqQw-QoSK6QPaois/edit?usp=sharing)| Valida Integração  Módulos Financeiro e Contabilidade      | 3-Avançado |






Referências:
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


https://www.youtube.com/watch?v=tIfEB66njB4&t=569s
https://www.ic.unicamp.br/~meidanis/courses/mc626/2014s1/materiais/slides/Aula15-Testes-caixa-preta-2-tabela-decisao-casos-uso.pdf
https://roadmap.sh/qa
https://www.guru99.com/v-model-software-testing.html
https://www.iso.org/obp/ui/en/#iso:std:iso-iec-ieee:29119:-3:ed-2:v1:en
https://softdesign.com.br/blog/a-importancia-do-teste-de-software/
