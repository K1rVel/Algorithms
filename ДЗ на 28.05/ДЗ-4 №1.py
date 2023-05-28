# Сложность алгоритма - O(log n)
def twoCitySchedCost(costs):
    totalCost = 0
    costs.sort(key=lambda x: x[0] - x[1])
    n = len(costs) // 2

    for i in range(n):
        totalCost += costs[i][0]

    for i in range(n, len(costs)):
        totalCost += costs[i][1]

    return totalCost