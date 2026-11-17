<div align="center">

# Pares de Notas Equilibradas — Tema 5

**Projeto e Análise de Algoritmos · CIESA · Ciência da Computação (4º Período)**

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Dependências](https://img.shields.io/badge/Dependencias-Zero%20Stdlib-00A86B?style=for-the-badge)
![Método](https://img.shields.io/badge/Metodo-Teste%20do%20Dobro-6F42C1?style=for-the-badge)
![Status](https://img.shields.io/badge/Codigo-Concluido-2EA44F?style=for-the-badge)

<br>

<img src="carimbo.png" alt="Carimbo de Julio Thiago" width="210">

<br><br>

[Sobre o Problema](#-sobre-o-problema) •
[Estratégias e Complexidade](#-estratégias-e-complexidade) •
[Análise Teórica](#-análise-teórica-tema-5) •
[Como Executar](#-como-executar) •
[Pipeline](#-pipeline-executado-automaticamente) •
[Estrutura](#-estrutura-do-repositório)

</div>

---

## Sobre o Problema

Para planejar dinâmicas em dupla equilibradas, a coordenação acadêmica precisa saber **quantos pares distintos de alunos** possuem diferença de nota de no máximo `d` pontos. Dada uma lista com `n` notas inteiras no intervalo `[0, 100]` e uma tolerância `d >= 0`, conta-se quantos pares `(i, j)` com `0 <= i < j < n` satisfazem:

$$\vert{}nota[i] - nota[j]\vert{} \le d$$

O projeto resolve o problema por múltiplas abordagens, instrumenta suas **operações básicas** separadamente (sem cronometrar tempo de máquina) e comprova suas classes assintóticas por meio do **Teste do Dobro** — observando a razão que estabiliza e a convergência da coluna `dobro = c(n) / c(n/2)`.

---

## Estratégias e Complexidade

Foram implementadas três versões completas em `tema5.py`:

| Versão | Função | Operação Básica Contada | Fase 1 (Ordenação) | Fase 2 (Contagem) | Melhor Caso | Caso Médio | Pior Caso |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **1. Ingênua** | `contar_pares_ingenua` | Comparações entre pares | — | $\Theta(n^2)$ | $\Theta(n^2)$ | $\Theta(n^2)$ | $\Theta(n^2)$ |
| **2. Esperta** | `contar_pares_ordenada_binaria` | Comparações + voltas da busca | $\Theta(n \log n)$ | $\Theta(n \log n)$ | $\Theta(n \log n)$ | $\Theta(n \log n)$ | $\Theta(n \log n)$ |
| **3. Extra** | `contar_pares_dois_ponteiros` | Comparações + passos da janela | $\Theta(n \log n)$ | $\Theta(n)$ | $\Theta(n \log n)$ | $\Theta(n \log n)$ | $\Theta(n \log n)$ |

### Como cada abordagem funciona

1. **Ingênua (`contar_pares_ingenua`):** Percorre todos os pares `(i, j)` com `i < j` por meio de dois laços aninhados, executando exatamente `n(n - 1) / 2` comparações independentemente dos valores das notas.
2. **Esperta (`contar_pares_ordenada_binaria`):** Ordena a lista com `mergesort` e, para cada posição `i`, aplica uma busca binária adaptada (`_ultimo_menor_ou_igual`) em `[i + 1 .. n - 1]` para localizar o último índice com nota `<= nota[i] + d`. A quantidade de pares válidos daquele aluno sai diretamente por `ultimo - i`.
3. **Extra (`contar_pares_dois_ponteiros`):** Após o `mergesort`, desliza uma janela `[esquerda .. direita)` pela lista ordenada. Como o ponteiro `direita` apenas avança (nunca retrocede), a varredura executa no máximo `2n` comparações, reduzindo a **Fase 2** para $\Theta(n)$.

---

## Análise Teórica (Tema 5)

<details open>
<summary><b>1. A classe assintótica muda com o valor de <code>d</code> (<code>d = 0</code>, <code>d = 5</code>, <code>d = 100</code>)?</b></summary>

<br>

**Não.**
- Na **versão ingênua**, os dois laços sempre testam todos os `n(n - 1) / 2` pares sem parada antecipada ($\Theta(n^2)$ para qualquer `d`).
- Nas **versões espertas**, o `mergesort` executa $\Theta(n \log n)$ comparações antes mesmo de `d` ser consultado, dominando o custo assintótico total em todos os cenários. Variar `d` altera apenas as constantes da Fase 2.

</details>

<details open>
<summary><b>2. Por que contar os pares é mais rápido do que listá-los?</b></summary>

<br>

Porque a contagem calcula quantos elementos cabem no intervalo válido por **aritmética de índices** (`ultimo - i` ou `direita - 1 - esquerda`) em tempo $O(1)$ por aluno, alcançando $\Theta(n \log n)$ no total.

Se o algoritmo precisasse **listar** cada par, o custo mínimo seria limitado pelo tamanho da própria saída. Em uma entrada onde todas as notas são iguais (ex.: `[50, 50, ..., 50]`) ou quando `d = 100`, **todos** os `n(n - 1) / 2` pares são válidos — logo, apenas construir ou imprimir a lista de pares já custaria $\Theta(n^2)$, igualando a versão ingênua.

</details>

<details open>
<summary><b>3. Busca Binária vs. Dois Ponteiros (Versão Extra)</b></summary>

<br>

Embora ambas apresentem custo total $\Theta(n \log n)$ devido ao `mergesort`, a medição isolada da **Fase 2** na série estendida (`n` até `100.000`) comprova a diferença estrutural:
- **Busca Binária:** estabiliza em `c / (n log2 n)` com fator `dobro` próximo de `2.13`.
- **Dois Ponteiros:** estabiliza em `c / n` com fator `dobro = 2.00`.

</details>

---

## Como Executar

O projeto utiliza apenas bibliotecas padrão do Python 3 (`csv`, `math`, `random`, `sys`). Na raiz do repositório, execute:

```bash
python3 tema5.py
```

### Pipeline executado automaticamente

1. **Validação de Correção (`validar_correcao`):** Verifica a equivalência exata entre as três versões em **10 casos de borda** (lista vazia, 1 elemento, todas iguais, repetidas e extremos `0` e `100`) e em **1.000 entradas aleatórias**.
2. **Parte A — Caso Médio (`n = 100` a `1.600`):** Calcula a média de **30 amostras aleatórias** com sementes fixas para `d` em `{0, 5, 100}`, reportando o total e cada fase separadamente.
3. **Parte B — Série Estendida (`n = 12.500` a `100.000`):** Avalia as versões espertas para `d = 5` em entradas de grande porte.
4. **Parte C — Melhor e Pior Caso Explícitos:** Mede entradas determinísticas construídas com `ordenado(n)`, `invertido(n)` e `[50] * n`.
5. **Exportação:** Grava todas as séries no arquivo `medicoes.csv`.

---

## Estrutura do Repositório

```text
├── tema5.py            # Implementações das 3 versões, testes de correção e experimentos
├── trabalho_base.py    # Base comum (mergesort, geradores, teste_do_dobro, salvar_csv)
├── medicoes.csv        # Dados brutos gerados automaticamente ao rodar tema5.py
├── carimbo.png         # Carimbo oficial de validação do trabalho
└── README.md           # Documentação do projeto
```

---
