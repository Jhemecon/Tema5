"""
Tema 5 — Pares de notas equilibradas.

O programa conta pares de alunos cujas notas diferem em no máximo d pontos.
Foram implementadas duas versões pedidas no enunciado:

1. comparação direta de todos os pares;
2. mergesort seguido de buscas binárias.

A versão extra com dois ponteiros não foi implementada, pois ficará para
outro integrante da equipe.
"""

from trabalho_base import aleatorio, mergesort, salvar_csv, teste_do_dobro


def contar_pares_ingenua(notas, distancia_maxima):
    """Conta os pares válidos testando cada par de notas."""
    pares = 0
    comparacoes = 0

    # Cada combinação i < j representa um par de alunos diferente.
    for i in range(len(notas)):
        for j in range(i + 1, len(notas)):
            comparacoes += 1
            if abs(notas[i] - notas[j]) <= distancia_maxima:
                pares += 1

    return pares, comparacoes


def _ultimo_menor_ou_igual(lista, limite, inicio, comparacoes):
    """Retorna o último índice com valor <= limite e as voltas da busca."""
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


def contar_pares_ordenada(notas, distancia_maxima):
    """Conta pares após ordenar, separando custos de ordenação e busca."""
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


def _medir_ingenua(n, distancia_maxima):
    notas = aleatorio(n, lo=0, hi=100, semente=42 + n)
    return contar_pares_ingenua(notas, distancia_maxima)[1]


def _medir_ordenada(n, distancia_maxima):
    notas = aleatorio(n, lo=0, hi=100, semente=42 + n)
    _, comparacoes_ordenacao, voltas_buscas = contar_pares_ordenada(
        notas, distancia_maxima
    )
    return comparacoes_ordenacao + voltas_buscas


def executar_experimentos():
    """Executa os casos pedidos e salva as medições brutas em CSV."""
    dados = []
    tamanhos = (100, 200, 400, 800, 1600)

    # O enunciado solicita testar d = 0, um d pequeno e d = 100.
    for distancia_maxima in (0, 5, 100):
        titulo_ingenua = f"Ingênua (d={distancia_maxima})"
        titulo_ordenada = f"Ordenada + busca binária (d={distancia_maxima})"

        teste_do_dobro(
            titulo_ingenua,
            lambda n, d=distancia_maxima: _medir_ingenua(n, d),
            tamanhos=tamanhos,
            versao=f"ingenua_d{distancia_maxima}",
            dados=dados,
        )
        teste_do_dobro(
            titulo_ordenada,
            lambda n, d=distancia_maxima: _medir_ordenada(n, d),
            tamanhos=tamanhos,
            versao=f"ordenada_busca_binaria_d{distancia_maxima}",
            dados=dados,
        )

    salvar_csv(dados)


if __name__ == "__main__":
    executar_experimentos()
