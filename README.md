<div align="center">

# 📊 Pares de Notas Equilibradas — Tema 5

**Projeto e Análise de Algoritmos · CIESA · Ciência da Computação (4º/6º Períodos)**

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Dependencies](https://img.shields.io/badge/Depend%C3%AAncias-Zero%20(Stdlib)-00A86B?style=for-the-badge)](trabalho_base.py)
[![Complexity](https://img.shields.io/badge/M%C3%A9todo-Teste%20do%20Dobro-6F42C1?style=for-the-badge)](tema5.py)
[![Status](https://img.shields.io/badge/C%C3%B3digo-Conclu%C3%ADdo-2EA44F?style=for-the-badge)](#-status-das-entregas)

<br>

<img src="carimbo.png" alt="Carimbo de Julio Thiago" width="210">

<br><br>

[Sobre o Problema](#-sobre-o-problema) •
[Estratégias e Complexidade](#-estratégias-e-complexidade) •
[Análise Teórica](#-análise-teórica-tema-5) •
[Como Executar](#-como-executar) •
[Prévia das Saídas](#-prévia-das-saídas) •
[Estrutura](#-estrutura-do-repositório)

</div>

---

## 🎯 Sobre o Problema

Para planejar dinâmicas em dupla equilibradas, a coordenação acadêmica precisa saber **quantos pares distintos de alunos** possuem diferença de nota de no máximo $d$ pontos. Formalmente, dada uma lista com $n$ notas inteiras no intervalo $[0, 100]$ e uma tolerância $d \ge 0$, busca-se a cardinalidade do conjunto:

$$\Big\vert{}\,\big\{\,(i, j) \;\big\vert{}\; 0 \le i < j < n \;\text{ e }\; \vert{}\text{nota}[i] - \text{nota}[j]\vert{} \le d\,\big\}\,\Big\vert{}$$

O objetivo do projeto é resolver o problema por múltiplas abordagens, instrumentar suas **operações básicas** separadamente (sem cronometrar tempo de máquina) e comprovar suas classes assintóticas por meio do **Teste do Dobro** — observando a razão que estabiliza e a convergência da coluna `dobro` $= c(n)/c(n/2)$.

> [!IMPORTANT]
> **Conformidade com as Regras da Disciplina:** Todas as soluções foram implementadas do zero utilizando exclusivamente o `mergesort` e os geradores determinísticos de `trabalho_base.py`. Não foram utilizadas funções ou estruturas prontas proibidas (`sorted`, `list.sort`, `bisect`, `set`, `dict`, `Counter` ou operador `in` em listas).

---

## ⚡ Estratégias e Complexidade

Foram implementadas três versões completas em `tema5.py`:

| Versão | Função | Operação Básica Contada | Fase 1 (Ordenação) | Fase 2 (Contagem) | Melhor Caso | Caso Médio | Pior Caso |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **1. Ingênua** | `contar_pares_ingenua` | Comparações entre pares | — | $\Theta(n^2)$ | $\Theta(n^2)$ | $\Theta(n^2)$ | $\Theta(n^2)$ |
| **2. Esperta** | `contar_pares_ordenada_binaria` | Comparações + voltas da busca | $\Theta(n \log n)$ | $\Theta(n \log n)$ | $\Theta(n \log n)$ | $\Theta(n \log n)$ | $\Theta(n \log n)$ |
| **3. Extra** | `contar_pares_dois_ponteiros` | Comparações + passos da janela | $\Theta(n \log n)$ | $\Theta(n)$ | $\Theta(n \log n)$ | $\Theta(n \log n)$ | $\Theta(n \log n)$ |

### Como cada abordagem funciona
1. **Ingênua:** Percorre todos os pares $(i, j)$ com $i < j$ por meio de dois laços aninhados, executando exatamente $\frac{n(n-1)}{2}$ comparações independentemente dos valores das notas.
2. **Esperta (Ordenação + Busca Binária):** Ordena a lista com `mergesort` e, para cada posição $i$, aplica uma busca binária adaptada (`_ultimo_menor_ou_igual`) em $[i+1 \dots n-1]$ para localizar o último índice com nota $\le \text{nota}[i] + d$. A quantidade de pares válidos daquele aluno é obtida diretamente por $\text{último} - i$.
3. **Extra (Ordenação + Dois Ponteiros):** Após o `mergesort`, desliza uma janela $[esquerda \dots direita)$ pela lista ordenada. Como o ponteiro `direita` apenas avança (nunca retrocede), a varredura executa no máximo $2n$ operações, reduzindo a **Fase 2** para $\Theta(n)$.

---

## 🧠 Análise Teórica (Tema 5)

<details open>
<summary><b>1. A classe assintótica muda com o valor de <code>d</code> (<code>d = 0</code>, <code>d = 5</code>, <code>d = 100</code>)?</b></summary>
<br>

**Não.**
* Na **versão ingênua**, os dois laços sempre testam todos os $\frac{n(n-1)}{2}$ pares sem parada antecipada ($\Theta(n^2)$ para qualquer $d$).
* Nas **versões espertas**, o `mergesort` executa $\Theta(n \log n)$ comparações antes mesmo de $d$ ser consultado, dominando o custo assintótico total em todos os cenários. Variar $d$ altera apenas as constantes da Fase 2.

</details>

<details>
<summary><b>2. Por que contar os pares é mais rápido do que listá-los?</b></summary>
<br>

Porque a contagem calcula quantos elementos cabem no intervalo válido por **aritmética de índices** (`ultimo - i` ou `direita - 1 - esquerda`) em tempo $O(1)$ por aluno, alcançando $\Theta(n \log n)$ no total.

Se o algoritmo precisasse **listar** cada par, o custo mínimo seria limitado pelo tamanho da própria saída ($\Omega(\text{saída})$). Em uma entrada onde todas as notas são iguais (ex.: `[50, 50, ..., 50]`) ou quando $d = 100$, **todos** os $\frac{n(n-1)}{2}$ pares são válidos — logo, apenas construir ou imprimir a lista de pares já custaria $\Theta(n^2)$, igualando a versão ingênua.

</details>

<details>
<summary><b>3. Busca Binária vs. Dois Ponteiros (Versão Extra)</b></summary>
<br>

Embora ambas apresentem custo total $\Theta(n \log n)$ devido ao `mergesort`, a medição isolada da **Fase 2** na série estendida ($n$ até $100.000$) comprova a diferença estrutural:
* **Busca Binária:** estabiliza em $c / (n \log_2 n)$ com fator `dobro` $\approx 2.13$.
* **Dois Ponteiros:** estabiliza em $c / n$ com fator `dobro` $= 2.00$.

</details>

---

## 🚀 Como Executar

O projeto utiliza apenas bibliotecas padrão do Python 3 (`csv`, `math`, `random`, `sys`). Na raiz do repositório, execute:

```bash
python3 tema5.py
