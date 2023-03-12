# from mochila import knapsack, knapsack_memo, knapsack_memo2
import random 
import time

# gera valores aleatorios baseado em quantos items e qual o peso maximo
def generate_values_and_weights(items, weight_limit):
    values = []
    weights = []
    for i in range(items):
        # valores de cada item varia de 1 a 100, enquanto os pesos podem variar ate o limite de peso
        values.append(random.randint(1, 100))
        weights.append(random.randint(1, weight_limit))
    return values, weights

def main():


    # in python, knapsack_memo can handle 5000 items and 2000 capacity
    # finishing in ~4 seconds


    # knapsack_memo pode lidar com 5000 itens e 2000 de capacidade
    # termina em ~4 segundos
    # knapsack

    values, weights = generate_values_and_weights(30, 100)
    capacity = 250

    fopen = open("test/values.txt", "w")
    while len(values) > 0:
        fopen.write(str(values.pop(0)))
        fopen.write("\n")
    fopen.close()

    fopen = open("test/weights.txt", "w")
    while len(weights) > 0:
        fopen.write(str(weights.pop(0)))
        fopen.write("\n")
    fopen.close()

    fopen = open("test/capacity.txt", "w")
    fopen.write(str(capacity))
    fopen.close()

main()