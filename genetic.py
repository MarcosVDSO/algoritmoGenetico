from random import getrandbits, randint, random

def individual(n_de_itens):
    """Cria um membro da população"""
    return [getrandbits(1) for _ in range(n_de_itens)]

def population(n_de_individuos, n_de_itens):
    """Cria a população"""
    return [individual(n_de_itens) for _ in range(n_de_individuos)]

def fitness(individuo, orcamento_maximo, itens):
    """Faz avaliação do indivíduo"""
    custo_total, necessidade_total = 0, 0
    for indice, valor in enumerate(individuo):
        custo_total += (individuo[indice] * itens[indice][0])
        necessidade_total += (individuo[indice] * itens[indice][1])
    if custo_total > orcamento_maximo:
        return -1  # Retorna -1 no caso de orçamento excedido
    return necessidade_total  # Retorna a soma da importância dos itens

def media_fitness(populacao, orcamento_maximo, itens):
    """Encontra a avaliação média da população"""
    validos = [fitness(x, orcamento_maximo, itens) for x in populacao if fitness(x, orcamento_maximo, itens) >= 0]
    if not validos:
        return 0
    return sum(validos) / len(validos)

def selecao_roleta(pais):
    """Seleciona um pai e uma mãe baseado nas regras da roleta"""
    def sortear(fitness_total, indice_a_ignorar=-1):
        """Monta roleta para realizar o sorteio"""
        roleta, acumulado, valor_sorteado = [], 0, random()
        if indice_a_ignorar != -1:
            fitness_total -= valores[0][indice_a_ignorar]
        for indice, i in enumerate(valores[0]):
            if indice_a_ignorar == indice:
                continue
            acumulado += i
            roleta.append(acumulado / fitness_total)
            if roleta[-1] >= valor_sorteado:
                return indice
    valores = list(zip(*pais))
    fitness_total = sum(valores[0])
    indice_pai = sortear(fitness_total)
    indice_mae = sortear(fitness_total, indice_pai)
    pai = valores[1][indice_pai]
    mae = valores[1][indice_mae]
    return pai, mae

def evolve(populacao, orcamento_maximo, itens, n_de_cromossomos, mutate=0.05):
    """Tabula cada indivíduo e o seu fitness"""
    pais = [[fitness(x, orcamento_maximo, itens), x] for x in populacao if fitness(x, orcamento_maximo, itens) >= 0]
    pais.sort(reverse=True)
    filhos = []
    while len(filhos) < n_de_cromossomos:
        homem, mulher = selecao_roleta(pais)
        meio = len(homem) // 2
        filho = homem[:meio] + mulher[meio:]
        filhos.append(filho)
    for individuo in filhos:
        if mutate > random():
            pos_to_mutate = randint(0, len(individuo) - 1)
            individuo[pos_to_mutate] = 1 - individuo[pos_to_mutate]
    return filhos