import time
import sys

sys.setrecursionlimit(10000)

# knapsack problem
# highest value possible without exceeding weight limit
def knapsack(values, weights, items, capacity):
    # caso base, quando nao ha mais itens ou quanto o limite de peso eh 0
    if items == 0 or capacity == 0:
        return 0
    # se o peso do item for maior que o limite de peso, nao o coloca na mochila
    if weights[items-1] > capacity:
        return knapsack(values, weights, items-1, capacity)
    else:
        # retorna o maior valor entre o valor do item + o valor que ja esta na mochila
        # e o valor que ja esta na mochila
        return max(values[items-1] + knapsack(values, weights, items-1, capacity-weights[items-1]),
                   knapsack(values, weights, items-1, capacity))

def knapsack_memo(values, weights, items, capacity):
    K = [[-1 for i in range(capacity+1)] for j in range(items+1)]
    for i in range(items+1):
        for j in range(capacity+1):
            if i == 0 or j == 0:
                K[i][j] = 0
            elif weights[i-1] <= j:
                K[i][j] = max(values[i-1] + K[i-1][j-weights[i-1]], K[i-1][j])
            else:
                K[i][j] = K[i-1][j]
    print(sys.getsizeof(K))
    return K[items][capacity]

def knapsack_memo2(values, weights, items, capacity, memo):
    # caso base, quando nao ha mais itens ou quanto o limite de peso eh 0
    if memo[items][capacity] != -1:
        return memo[items][capacity]
    if items == 0 or capacity == 0:
        return 0
    # se o peso do item for maior que o limite de peso, nao o coloca na mochila
    if weights[items-1] > capacity:
        return knapsack_memo2(values, weights, items-1, capacity, memo)
    else:
        # retorna o maior valor entre o valor do item + o valor que ja esta na mochila
        # e o valor que ja esta na mochila
        memo[items][capacity] = max(values[items-1] + knapsack_memo2(values, weights, items-1, capacity-weights[items-1], memo),
                                        knapsack_memo2(values, weights, items-1, capacity, memo))
        return memo[items][capacity]

def main():
    
    with open("test/capacity.txt", "r") as f:
        capacity = int(f.readline())

    with open("test/values.txt", "r") as f:
        # values = [int(x) for x in f.readline().split()]
        values = [int(x) for x in f.readlines()]

    with open("test/weights.txt", "r") as f:
        # weights = [int(x) for x in f.readline().split()]
        weights = [int(x) for x in f.readlines()]

    items = len(values)
    
    # values = [22, 74, 3, 82, 2, 35, 89, 79, 57, 41, 18, 15, 18, 40, 73, 46, 31, 2, 24, 36, 52, 84, 88, 37, 90, 76, 55, 91, 44, 7, 46, 54, 94, 54, 38, 91, 35, 79, 69, 88, 38, 32, 35, 10, 100, 93, 53, 91, 76, 13, 90, 49, 8, 46, 13, 48, 51, 70, 66, 85, 21, 78, 100, 80, 18, 81, 58, 19, 4, 32, 12, 59, 42, 39, 52, 51, 66, 77, 34, 91, 61, 2, 76, 62, 91, 54, 76, 5, 38, 79, 84, 50, 30, 38, 64, 12, 4, 18, 45, 47, 55, 46, 32, 3, 38, 73, 57, 99, 65, 77]
    # weights = [82, 5, 13, 61, 36, 67, 9, 18, 39, 69, 50, 26, 41, 17, 7, 7, 17, 41, 44, 41, 59, 69, 61, 56, 65, 96, 67, 100, 82, 100, 18, 12, 42, 3, 36, 44, 37, 77, 43, 81, 40, 32, 44, 29, 98, 35, 21, 29, 84, 37, 61, 64, 99, 6, 93, 81, 59, 5, 10, 69, 58, 86, 36, 66, 73, 26, 1, 95, 69, 68, 58, 95, 30, 2, 70, 5, 45, 33, 69, 13, 90, 25, 24, 35, 75, 36, 40, 10, 78, 17, 32, 98, 59, 28, 84, 89, 85, 58, 5, 15, 94, 22, 94, 85, 50, 75, 29, 83, 17, 8]
    # capacity = 100



    # print(capacity)
    # print(values)
    # print(weights)
    # print(items)


    print("\nTime for each function with", items, "items and", capacity, "weight limit\n")
    print("---------------------------------------------------------\n")

    # b = time.time()
    # print("Python Knapsack: ", knapsack(values, weights, items, capacity), "in ", time.time()-b, "seconds")

    # b = time.time() 
    # print("\nPython Knapsack with memo: ", knapsack_memo(values, weights, items, capacity), "in ", time.time()-b, "seconds")

    # b = time.time()
    # memo = [[-1 for x in range(capacity + 1)] for x in range(items + 1)]
    # print("\nPython Knapsack with memo (alternative): ", knapsack_memo2(values, weights, items, capacity, memo), "in ", time.time()-b, "seconds")

if __name__ == "__main__":
    main()