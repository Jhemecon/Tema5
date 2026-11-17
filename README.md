<div align="center">

# Pares de Notas Equilibradas — Tema 5
**Projeto e Análise de Algoritmos · CIESA · Ciência da Computação (4º/6º Períodos)**

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Implementado-2EA44F?style=for-the-badge)
![Complexidade](https://img.shields.io/badge/An%C3%A1lise-Teste%20do%20Dobro-8A2BE2?style=for-the-badge)

<br>

<img src="carimbo.png" alt="Carimbo de Julio Thiago" width="210">

</div>

---

## Sobre o Problema

Dada uma lista com as notas de $n$ alunos e uma tolerância $d$, o desafio consiste em **contar quantos pares distintos** $(i, j)$ com $i < j$ possuem notas equilibradas, ou seja:

$$\vert{}\text{nota}[i] - \text{nota}[j]\vert{} \le d$$

O projeto compara três abordagens distintas, contabiliza suas operações básicas separadamente e comprova suas classes de complexidade assintótica por meio do **Teste do Dobro**[cite: 14, 17, 21, 22].

---

## Comparativo das Estratégias

| Estratégia | Função em `tema5.py` | Operação Contada | Fase 1 (Ordenação) | Fase 2 (Contagem) | Custo Total |
| :--- | :--- | :--- | :---: | :---: | :---: |
| **1. Ingênua** | `contar_pares_ingenua` | Comparações entre pares | — | $\Theta(n^2)$ | **$\Theta(n^2)$** |
| **2. Esperta** | `contar_pares_ordenada_binaria` | Comparações + voltas da busca | $\Theta(n \log n)$ | $\Theta(n \log n)$ | **$\Theta(n \log n)$** |
| **3. Extra** | `contar_pares_dois_ponteiros` | Comparações + passos da janela | $\Theta(n \log n)$ | $\Theta(n)$ | **$\Theta(n \log n)$** |

> **Destaque técnico:** Embora as versões **Esperta** e **Extra** pertençam à mesma classe total $\Theta(n \log n)$ por conta do `mergesort`, isolar a **Fase 2** na série estendida ($n$ até $100.000$) evidencia a queda de $\Theta(n \log n)$ (busca binária) para $\Theta(n)$ (janela deslizante).

---

## Como Executar

Certifique-se de ter o **Python 3** instalado e execute o comando abaixo na raiz do repositório[cite: 20, 21, 22]:

```bash
python3 tema5.py
