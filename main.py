# Importações necessárias
from genetic import *
from matplotlib import pyplot as plt

# Definição dos itens (Preço e Necessidade)
itens = [
    [22, 10],  # Arroz (5kg)
    [3, 5],    # Açúcar (2kg)
    [8, 6],    # Óleo (1l)
    [5, 10],   # Feijão (1kg)
    [5, 8],    # Macarrão (500g)
    [5, 7],    # Sardinha (1 lata)
    [32, 9],   # Carne (1kg)
    [13, 9],   # Frango (1kg)
    [8, 5],    # Queijo (200g)
    [4, 5],    # Presunto (200g)
    [6, 6],    # Pão (8un.)
    [4, 7],    # Banana (1kg)
    [2, 7],    # Laranja (1kg)
    [7, 2],    # Abacate (1kg)
    [2, 9],    # Sabão (1un.)
    [4, 6],    # Limpador multiuso (1un.)
    [7, 1],    # Água Tônica (500ml)
    [6, 4],    # Polpa de Fruta (500ml)
    [8, 3],    # Refrigerante (2l)
    [6, 2]     # Cerveja (600ml)
]

orcamento_maximo = 75  # Orçamento disponível
n_de_cromossomos = 150
geracoes = 150
n_de_itens = len(itens)

# Execução dos procedimentos
populacao = population(n_de_cromossomos, n_de_itens)
historico_de_fitness = [media_fitness(populacao, orcamento_maximo, itens)]

for i in range(geracoes):
    populacao = evolve(populacao, orcamento_maximo, itens, n_de_cromossomos)
    historico_de_fitness.append(media_fitness(populacao, orcamento_maximo, itens))

# Prints do terminal
for indice, dados in enumerate(historico_de_fitness):
    print("Geracao: ", indice, " | Media de importância: ", dados)

print("\nOrçamento máximo: R$", orcamento_maximo, "\n\nItens disponíveis:")
for indice, i in enumerate(itens):
    print(f"Item {indice+1}: R${i[0]} | Necessidade: {i[1]}")

print("\nExemplos de boas soluções: ")
for i in range(5):
    print(populacao[i])

# Gerador de gráfico
plt.plot(range(len(historico_de_fitness)), historico_de_fitness)
plt.grid(True, zorder=0)
plt.title("Problema da seleção de compras")
plt.xlabel("Geração")
plt.ylabel("Importância média dos itens")
plt.show()
