from mochila import knapsack, knapsack_memo, knapsack_tabu
import time

def main():    
    with open("test/capacity.txt", "r") as f:
        capacity = int(f.readline())

    with open("test/values.txt", "r") as f:
        values = [int(x) for x in f.readlines()]

    with open("test/weights.txt", "r") as f:
        weights = [int(x) for x in f.readlines()]
    items = len(values)



    # print(capacity)
    # print(values)
    # print(weights)
    # print(items)

    print("\nTime for each function with", items, "items and", capacity, "weight limit\n")
    print("---------------------------------------------------------\n")

    # demorou 426.5 segundos para rodar com 60 itens e 250 de capacidade maxima
    b = time.perf_counter()
    print("Recursive Knapsack: ", knapsack(values, weights, items, capacity), "in ", time.perf_counter()-b, "seconds")

    # demorou 0.004 segundos para rodar com 60 itens e 250 de capacidade maxima
    b = time.perf_counter() 
    print("\nMemo Knapsack: ", knapsack_memo(values, weights, items, capacity), "in ", time.perf_counter()-b, "seconds")

    # demorou 0.002 segundos para rodar com 60 itens e 250 de capacidade maxima
    # na maioria das vezes acaba nao acertando o resultado otimo global, porem
    # sempre acaba resultando numa combinacao otima em relacao a capacidade maxima
    b = time.perf_counter()
    print("\nTabu Knapsack: ", knapsack_tabu(values, weights, items, capacity), "in ", time.perf_counter()-b, "seconds")


if __name__ == "__main__":
    main()