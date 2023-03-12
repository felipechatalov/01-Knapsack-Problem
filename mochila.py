import time
import sys

sys.setrecursionlimit(10000)

# problema da mochila
# maior valor possivel de itens sem exceder o limite de peso
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
    # cria o array para memorizar os resultados
    K = [[-1 for i in range(capacity+1)] for j in range(items+1)]
    for i in range(items+1):
        for j in range(capacity+1):
            # caso base, quando nao ha mais itens ou quanto o limite de peso eh 0
            if i == 0 or j == 0:
                K[i][j] = 0
            elif weights[i-1] <= j:
                K[i][j] = max(values[i-1] + K[i-1][j-weights[i-1]], K[i-1][j])
            else:
                K[i][j] = K[i-1][j]
    # print(f"Uso de memoria para o memo: {sys.getsizeof(K)}")
    return K[items][capacity]

def get_knapsack_value(config, values, weights, items, capacity):
    # retorna o valor da configuracao atual de itens na mochila
    # caso o peso passe da capacidade max, retorna 0
    value = 0
    w = 0
    for i in range(items):
        value += config[i] * values[i]
        w += config[i] * weights[i]
    return [value, w] if w <= capacity else [0, 0]

def get_neightbours(solution, values, weights, items, capacity):
    results_sol = [] # lista de solucoes vizinhas
    results_val = [] # lista de valores das solucoes vizinhas
    for i in range(items):
        # inverte o valor do item i
        solution[i] = 1 - solution[i] 
        # adiciona a solucao vizinha, precisa ser uma copia para nao mandar um ponteiro
        # e alterar a solucao original
        results_sol.append(solution.copy())
        # adiciona o valor da solucao vizinha
        r, _ = get_knapsack_value(solution, values, weights, items, capacity)
        results_val.append(r) 
        # inverte o valor do item i novamente para voltar a solucao original
        solution[i] = 1 - solution[i] 
    return results_sol, results_val

def knapsack_tabu(values, weights, items, capacity):
    # inicializa a melhor solucao com 0 em todos os itens
    # melhor valor, no caso 0 ate o momento e o tempo sem progresso
    solucoes_vistas = []
    best_sol = [0 for i in range(items)]
    solucoes_vistas.append(best_sol)
    best_val = 0
    iter_wout_progress = 0
    # numero arbitrario de iteracoes sem progresso
    while iter_wout_progress < items:
        # pega as solucoes vizinhas e seus valores
        configs, n_values = get_neightbours(best_sol, values, weights, items, capacity)
        # print(configs)
        # print(n_values)
        # pega a melhor solucao vizinha e considera-se a melhor atual
        for i in range(len(n_values)):
            if n_values[i] > best_val and configs[i] not in solucoes_vistas:
                best_val = n_values[i]
                best_sol = configs[i]
                solucoes_vistas.append(best_sol)
                # print("progress: ", best_sol)
                # reseta o contador de iteracoes sem progresso, ou adiciona 1 caso nao tenhamos progresso
                iter_wout_progress = 0
            else:
                iter_wout_progress += 1

    r, s = get_knapsack_value(best_sol, values, weights, items, capacity)
    # print(best_sol)
    # print(r, s)
    return best_val


def main():
    # valores dos itens
    values = [60, 100, 120]
    # pesos dos itens
    weights = [10, 20, 30]
    # numero de itens
    items = len(values)
    # capacidade maxima da mochila
    capacity = 50

    print(knapsack(values, weights, items, capacity))
    print(knapsack_memo(values, weights, items, capacity))
    print(knapsack_tabu(values, weights, items, capacity))


if __name__ == "__main__":
    main()