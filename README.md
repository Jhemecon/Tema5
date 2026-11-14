# Trabalho PAA — Tema 5

![Carimbo de Julio Thiago](carimbo.png)

## Sobre o trabalho

Este trabalho da disciplina de Projeto e Análise de Algoritmos analisa o
problema de **pares de notas equilibradas**.

Dada uma lista com as notas dos alunos e um valor `d`, o objetivo é contar
quantos pares de alunos possuem diferença entre as notas menor ou igual a
`d`.

O trabalho compara diferentes estratégias, contabiliza as operações
realizadas e permite observar a classe de complexidade de cada solução.

## O que já foi feito

No arquivo [tema5.py](tema5.py) foram implementadas:

- **Versão ingênua:** testa todos os pares de notas e conta as comparações.
- **Versão otimizada:** ordena as notas usando o mergesort da base e usa
  buscas binárias para encontrar o limite de cada grupo de pares válidos.
- Contagem separada das comparações do mergesort e das voltas das buscas
  binárias.
- Experimentos para `d = 0`, `d = 5` e `d = 100`.
- Geração de tabelas de medições e do arquivo `medicoes.csv`.
- Comentários no código explicando as etapas principais.

As funções comuns utilizadas pelo trabalho estão em
[trabalho_base.py](trabalho_base.py).

## O que ainda falta fazer

- Implementar a versão extra com **dois ponteiros**, que ficou reservada para
  outro integrante da equipe.
- Fazer a análise escrita completa das entradas de melhor e pior caso.
- Comparar formalmente as classes de complexidade e organizar a apresentação
  final do trabalho.

## Como executar

No terminal, dentro da pasta do projeto:

```bash
python3 tema5.py
```

O programa imprime as tabelas de contagem e cria o arquivo `medicoes.csv`
com os dados brutos dos experimentos.

## Arquivos principais

- `tema5.py`: implementações e experimentos do Tema 5.
- `trabalho_base.py`: funções comuns de ordenação, geração de dados e medição.
- `carimbo.png`: carimbo utilizado neste trabalho.
