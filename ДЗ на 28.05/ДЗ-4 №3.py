# Сложность алгоритма - O(n)
def tribonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1

    a, b, c = 0, 1, 1
    curr = 3

    while curr <= n:
        a, b, c = b, c, a + b + c