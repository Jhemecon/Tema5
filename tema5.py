"""
Tema 5 — Pares de notas equilibradas.

O programa conta pares de alunos cujas notas diferem em no máximo d pontos.
Foram implementadas as três versões pedidas no enunciado:

1. Versão ingênua: comparação direta de todos os pares (i < j);
2. Versão esperta: mergesort seguido de buscas binárias;
3. Versão extra (dois ponteiros): mergesort seguido de janela deslizante.
"""

from trabalho_base import (
    aleatorio,
    invertido,
    mergesort,
    ordenado,
    salvar_csv,
    teste_do_dobro
)

AMOSTRAS_CASO_MEDIO = 30
TAMANHOS_BASE = (100, 200, 400, 800, 1600)
TAMANHOS_ESPERTA_ESTENDIDA = (12500, 25000, 50000, 100000)

#Versão ingênua
def contar_pares_ingenua(notas, distancia_maxima):
    """Conta os pares válidos testando cada par (i, j) com i < j."""
    pares = 0
    comparacoes = 0

    # Cada combinação i < j representa um par de alunos diferente.
    for i in range(len(notas)):
        for j in range(i + 1, len(notas)):
            comparacoes += 1
            if abs(notas[i] - notas[j]) <= distancia_maxima:
                pares += 1

    return pares, comparacoes

#Versão esperta
def _ultimo_menor_ou_igual(lista, limite, inicio, comparacoes):
    """Retorna o último índice com valor <= limite e atualiza voltas da busca."""
    esquerda = inicio
    direita = len(lista) - 1
    ultimo = inicio - 1

    # Esta busca é uma adaptação da busca binária da base para um limite.
    while esquerda <= direita:
        comparacoes += 1
        meio = (esquerda + direita) // 2
        if lista[meio] <= limite:
            ultimo = meio
            esquerda = meio + 1
        else:
            direita = meio - 1

    return ultimo, comparacoes


def contar_pares_ordenada_binaria(notas, distancia_maxima):
    """Ordena com mergesort e usa busca binária para achar o limite de cada nota."""
    ordenadas, comparacoes_ordenacao = mergesort(notas)
    pares = 0
    voltas_buscas = 0

    # Para cada nota, buscamos apenas até onde a diferença ainda é válida.
    # O início da busca é i + 1 para contar cada par uma única vez.
    for i, nota in enumerate(ordenadas):
        ultimo, voltas_buscas = _ultimo_menor_ou_igual(
            ordenadas, nota + distancia_maxima, i + 1, voltas_buscas
        )
        pares += max(0, ultimo - i)

    return pares, comparacoes_ordenacao, voltas_buscas


#Versão dois ponteiros
def contar_pares_dois_ponteiros(notas, distancia_maxima):
    """Ordena com mergesort e desliza uma janela [esquerda..direita)."""
    ordenadas, comparacoes_ordenacao = mergesort(notas)
    n = len(ordenadas)
    pares = 0
    comparacoes_janela = 0
    direita = 0

    # A cada passo, a janela desliza para a direita, mantendo a diferença válida.
    # O ponteiro da direita só avança, nunca retrocede, garantindo O(n) de complexidade.
    for esquerda in range(n):
        if direita <= esquerda:
            direita = esquerda + 1

        while direita < n:
            comparacoes_janela += 1
            if ordenadas[direita] - ordenadas[esquerda] <= distancia_maxima:
                direita += 1
            else:
                break

        pares += direita - 1 - esquerda

    return pares, comparacoes_ordenacao, comparacoes_janela


#Teste automatico de correção
def validar_correcao():
    """Valida casos de borda e 1.000 entradas aleatórias antes das medições."""
    casos_borda = [
        ([], 0),
        ([], 10),
        ([5], 0),
        ([5], 100),
        ([7, 7, 7, 7], 0),
        ([7, 7, 7, 7], 5),
        ([10, 20, 20, 30, 30, 30], 0),
        ([10, 20, 20, 30, 30, 30], 10),
        ([0, 100], 100),
        ([0, 100], 99),
    ]

    for lista, d in casos_borda:
        r_ing = contar_pares_ingenua(lista, d)[0]
        r_bin = contar_pares_ordenada_binaria(lista, d)[0]
        r_dp = contar_pares_dois_ponteiros(lista, d)[0]
        assert r_ing == r_bin == r_dp, (
            f"Divergência na borda {lista} (d={d}): "
            f"ing={r_ing}, bin={r_bin}, dp={r_dp}"
        )

    for teste in range(1000):
        n = (teste % 50) + 1
        d = teste % 101
        notas = aleatorio(n, lo=0, hi=100, semente=1000 + teste)
        r_ing = contar_pares_ingenua(notas, d)[0]
        r_bin = contar_pares_ordenada_binaria(notas, d)[0]
        r_dp = contar_pares_dois_ponteiros(notas, d)[0]
        assert r_ing == r_bin == r_dp, (
            f"Divergência no teste {teste} (n={n}, d={d}): "
            f"ing={r_ing}, bin={r_bin}, dp={r_dp}"
        )

    print("OK: Casos de borda e 1.000 entradas aleatórias validados com sucesso.")


#Funções auxiliares para medições de contagem de comparações
def _media_ingenua(n, distancia_maxima, amostras=AMOSTRAS_CASO_MEDIO):
    total = 0
    for k in range(amostras):
        notas = aleatorio(n, lo=0, hi=100, semente=42 + n * 100 + k)
        total += contar_pares_ingenua(notas, distancia_maxima)[1]
    return total / amostras


def _media_binaria(n, distancia_maxima, fase="total", amostras=AMOSTRAS_CASO_MEDIO):
    total = 0
    for k in range(amostras):
        notas = aleatorio(n, lo=0, hi=100, semente=42 + n * 100 + k)
        _, comp_ord, voltas_buscas = contar_pares_ordenada_binaria(
            notas, distancia_maxima
        )
        if fase == "ordenacao":
            total += comp_ord
        elif fase == "busca":
            total += voltas_buscas
        else:
            total += comp_ord + voltas_buscas
    return total / amostras


def _media_dois_ponteiros(n, distancia_maxima, fase="total", amostras=AMOSTRAS_CASO_MEDIO):
    total = 0
    for k in range(amostras):
        notas = aleatorio(n, lo=0, hi=100, semente=42 + n * 100 + k)
        _, comp_ord, comp_janela = contar_pares_dois_ponteiros(
            notas, distancia_maxima
        )
        if fase == "ordenacao":
            total += comp_ord
        elif fase == "janela":
            total += comp_janela
        else:
            total += comp_ord + comp_janela
    return total / amostras


def _medir_caso_extremo_binaria(entrada, distancia_maxima):
    _, comp_ord, voltas_buscas = contar_pares_ordenada_binaria(
        entrada, distancia_maxima
    )
    return comp_ord + voltas_buscas


def _medir_caso_extremo_dois_ponteiros(entrada, distancia_maxima):
    _, comp_ord, comp_janela = contar_pares_dois_ponteiros(
        entrada, distancia_maxima
    )
    return comp_ord + comp_janela


# Executa todos os experimentos e exporta os dados brutos para CSV
def executar_experimentos():
    """Executa todos os cenários do Tema 5 e exporta os dados brutos para CSV."""
    dados = []

    for d in (0, 5, 100):
        print("\n" + "=" * 72)
        print(f"CENÁRIO CASO MÉDIO: d = {d} (Média de {AMOSTRAS_CASO_MEDIO} entradas aleatórias)")
        print("=" * 72)

        teste_do_dobro(
            f"Ingênua — Total (d={d})",
            lambda n, dist=d: _media_ingenua(n, dist),
            tamanhos=TAMANHOS_BASE,
            versao=f"ingenua_d{d}",
            dados=dados,
        )

        teste_do_dobro(
            f"Esperta Busca Binária — Total [Ordenação + Buscas] (d={d})",
            lambda n, dist=d: _media_binaria(n, dist, fase="total"),
            tamanhos=TAMANHOS_BASE,
            versao=f"esperta_binaria_total_d{d}",
            dados=dados,
        )
        teste_do_dobro(
            f"Esperta Busca Binária — Fase 1: Ordenação (d={d})",
            lambda n, dist=d: _media_binaria(n, dist, fase="ordenacao"),
            tamanhos=TAMANHOS_BASE,
            versao=f"esperta_binaria_fase_ordenacao_d{d}",
            dados=dados,
        )
        teste_do_dobro(
            f"Esperta Busca Binária — Fase 2: Buscas Binárias (d={d})",
            lambda n, dist=d: _media_binaria(n, dist, fase="busca"),
            tamanhos=TAMANHOS_BASE,
            versao=f"esperta_binaria_fase_busca_d{d}",
            dados=dados,
        )

        teste_do_dobro(
            f"Extra Dois Ponteiros — Total [Ordenação + Janela] (d={d})",
            lambda n, dist=d: _media_dois_ponteiros(n, dist, fase="total"),
            tamanhos=TAMANHOS_BASE,
            versao=f"extra_dois_ponteiros_total_d{d}",
            dados=dados,
        )
        teste_do_dobro(
            f"Extra Dois Ponteiros — Fase 1: Ordenação (d={d})",
            lambda n, dist=d: _media_dois_ponteiros(n, dist, fase="ordenacao"),
            tamanhos=TAMANHOS_BASE,
            versao=f"extra_dois_ponteiros_fase_ordenacao_d{d}",
            dados=dados,
        )
        teste_do_dobro(
            f"Extra Dois Ponteiros — Fase 2: Janela Deslizante (d={d})",
            lambda n, dist=d: _media_dois_ponteiros(n, dist, fase="janela"),
            tamanhos=TAMANHOS_BASE,
            versao=f"extra_dois_ponteiros_fase_janela_d{d}",
            dados=dados,
        )

    print("\n" + "=" * 72)
    print("SÉRIE ESTENDIDA — VERSÕES ESPERTAS (d = 5)")
    print("=" * 72)

    teste_do_dobro(
        "Esperta Busca Binária Estendida — Total (d=5)",
        lambda n: _media_binaria(n, 5, fase="total", amostras=5),
        tamanhos=TAMANHOS_ESPERTA_ESTENDIDA,
        versao="esperta_binaria_estendida_total_d5",
        dados=dados,
    )
    teste_do_dobro(
        "Esperta Busca Binária Estendida — Apenas Buscas (d=5)",
        lambda n: _media_binaria(n, 5, fase="busca", amostras=5),
        tamanhos=TAMANHOS_ESPERTA_ESTENDIDA,
        versao="esperta_binaria_estendida_busca_d5",
        dados=dados,
    )
    teste_do_dobro(
        "Extra Dois Ponteiros Estendida — Total (d=5)",
        lambda n: _media_dois_ponteiros(n, 5, fase="total", amostras=5),
        tamanhos=TAMANHOS_ESPERTA_ESTENDIDA,
        versao="extra_dois_ponteiros_estendida_total_d5",
        dados=dados,
    )
    teste_do_dobro(
        "Extra Dois Ponteiros Estendida — Apenas Janela (d=5)",
        lambda n: _media_dois_ponteiros(n, 5, fase="janela", amostras=5),
        tamanhos=TAMANHOS_ESPERTA_ESTENDIDA,
        versao="extra_dois_ponteiros_estendida_janela_d5",
        dados=dados,
    )

    print("\n" + "=" * 72)
    print("MELHOR E PIOR CASO EXPLÍCITOS POR VERSÃO")
    print("=" * 72)

    # Ingênua: sempre faz n*(n-1)/2 comparações (melhor caso == pior caso)
    teste_do_dobro(
        "Ingênua — Melhor Caso (lista ordenada, d=0, nenhum par válido)",
        lambda n: contar_pares_ingenua(ordenado(n), 0)[1],
        tamanhos=TAMANHOS_BASE,
        versao="ingenua_melhor_caso",
        dados=dados,
    )
    teste_do_dobro(
        "Ingênua — Pior Caso (notas todas iguais, d=100, todos os pares válidos)",
        lambda n: contar_pares_ingenua([50] * n, 100)[1],
        tamanhos=TAMANHOS_BASE,
        versao="ingenua_pior_caso",
        dados=dados,
    )

    teste_do_dobro(
        "Esperta Busca Binária — Melhor Caso (ordenado(n), d=0)",
        lambda n: _medir_caso_extremo_binaria(ordenado(n), 0),
        tamanhos=TAMANHOS_BASE,
        versao="esperta_binaria_melhor_caso",
        dados=dados,
    )
    teste_do_dobro(
        "Esperta Busca Binária — Pior Caso (invertido(n), d=100)",
        lambda n: _medir_caso_extremo_binaria(invertido(n), 100),
        tamanhos=TAMANHOS_BASE,
        versao="esperta_binaria_pior_caso",
        dados=dados,
    )

    teste_do_dobro(
        "Extra Dois Ponteiros — Melhor Caso (ordenado(n), d=0)",
        lambda n: _medir_caso_extremo_dois_ponteiros(ordenado(n), 0),
        tamanhos=TAMANHOS_BASE,
        versao="extra_dois_ponteiros_melhor_caso",
        dados=dados,
    )
    teste_do_dobro(
        "Extra Dois Ponteiros — Pior Caso (invertido(n), d=5)",
        lambda n: _medir_caso_extremo_dois_ponteiros(invertido(n), 5),
        tamanhos=TAMANHOS_BASE,
        versao="extra_dois_ponteiros_pior_caso",
        dados=dados,
    )

    salvar_csv(dados)


if __name__ == "__main__":
    validar_correcao()
    executar_experimentos()