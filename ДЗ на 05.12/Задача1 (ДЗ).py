class Solution:    # Сложность = O(n)
                   # Num - число, с которым совершаем действие(уменьшаем до нуля)
                   # Int - кол-во шагов, которое нужно совершить с числом (Num)
                   # a - считает количество шагов

    def numberOfSteps(self, num: int) -> int:
        a = 0
        while num > 0:
            if num % 2: num -= 1
            else: num /= 2
            a += 1
        return a

