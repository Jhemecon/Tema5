# Trabalho PAA — Tema 5: Pares de Notas Equilibradas

<img src="carimbo.png" alt="Carimbo de Julio Thiago" width="220">

## Sobre o trabalho

Projeto prático da disciplina de **Projeto e Análise de Algoritmos (CIESA — 4º/6º períodos)** dedicado à análise empírica e teórica do problema **Pares de Notas Equilibradas**[cite: 14, 17, 22].

Dada uma lista com as notas de $n$ alunos e uma distância máxima $d$, o objetivo é contar quantos pares distintos $(i, j)$ com $i < j$ satisfazem $|nota[i] - nota[j]| \le d$, instrumentando as operações básicas para identificar suas classes assintóticas pelo **Teste do Dobro**[cite: 14, 17, 21, 22].

---

## Abordagens Implementadas

O arquivo `tema5.py` contém três soluções completas, utilizando exclusivamente os utilitários de [trabalho_base.py](trabalho_base.py)[cite: 20, 21, 22]:

1. **Versão Ingênua (`contar_pares_ingenua`):**
   * Compara diretamente todos os pares $(i, j)$ com $i < j$ usando dois laços aninhados[cite: 21].
   * **Operação contada:** comparações de diferença entre notas ($\Theta(n^2)$)[cite: 17, 21].

2. **Versão Esperta (`contar_pares_ordenada_binaria`):**
   * Ordena a lista com `mergesort` e, para cada aluno $i$, aplica uma busca binária adaptada (`_ultimo_menor_ou_igual`) para encontrar o maior índice cuja nota é $\le nota[i] + d$, somando `ultimo - i` pares sem percorrê-los um a um[cite: 17, 21].
   * **Operações contadas (separadas e somadas):** comparações da ordenação ($\Theta(n \log n)$) e voltas da busca binária ($\Theta(n \log n)$)[cite: 17, 21].

3. **Versão Extra — Janela Deslizante (`contar_pares_dois_ponteiros`):**
   * Ordena a lista com `mergesort` e mantém dois ponteiros (`esquerda` e `direita`) que avançam monotonicamente sem retroceder[cite: 17, 21].
   * **Operações contadas (separadas e somadas):** comparações da ordenação ($\Theta(n \log n)$) e comparações da janela deslizante ($\Theta(n)$)[cite: 17, 21].

---

## Estrutura dos Experimentos (`tema5.py`)

Ao executar o script principal, o programa realiza automaticamente quatro etapas:

* **Validação de Correção (`validar_correcao`):** Verifica a equivalência das três versões em 10 casos de borda (lista vazia, um elemento, todas as notas iguais, repetidas e limites `0` e `100`) e em **1.000 entradas aleatórias** antes de iniciar qualquer medição[cite: 20, 21].
* **Caso Médio (`Parte A`):** Mede a média de **30 entradas aleatórias** (com sementes fixas) para $n \in \{100, 200, 400, 800, 1600\}$ nos cenários $d = 0$, $d = 5$ e $d = 100$, exibindo tabelas tanto do custo total quanto de cada fase isolada[cite: 17, 20, 21].
* **Série Estendida (`Parte B`):** Avalia as versões espertas para $n \in \{12.500, 25.000, 50.000, 100.000\}$ ($d = 5$), evidenciando a estabilização de $c/(n \log_2 n)$ no custo total e a diferença entre $\Theta(n \log n)$ (busca binária) e $\Theta(n)$ (dois ponteiros) na fase pós-ordenação[cite: 17, 20, 21].
* **Melhor e Pior Caso Explícitos (`Parte C`):** Mede entradas extremas construídas com `ordenado(n)`, `invertido(n)` e notas constantes (`[50] * n`) para cada versão[cite: 20, 21].

---

## Como Reproduzir

Certifique-se de que `tema5.py` e `trabalho_base.py` estejam no mesmo diretório e execute[cite: 20, 21]:

```bash
python3 tema5.py
## Arquivos principais

- `tema5.py`: implementações e experimentos do Tema 5.
- `trabalho_base.py`: funções comuns de ordenação, geração de dados e medição.
- `carimbo.png`: carimbo utilizado neste trabalho.
