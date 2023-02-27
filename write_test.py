# from mochila import knapsack, knapsack_memo, knapsack_memo2
import random 
import time

def generate_values_and_weights(items, weight_limit):
    values = []
    weights = []
    for i in range(items):
        values.append(random.randint(1, 100))
        weights.append(random.randint(1, weight_limit))
    return values, weights


def main():

    # for python, knapsack...

    # for python, knapsack_memo can handle 5000 items and 2000 capacity
    # finishing in ~4 seconds


    values, weights = generate_values_and_weights(517, 100)
    capacity = 1000

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