class Solution(object):                    # Сложность = O(n)
    def minimumAbsDifference(self, arr):   # сортирую список
        arr.sort()                         # создаю переменную 'dif' = разница
        dif = float('inf')                 # высчитываю разницу между двумя ближними элементами в списке
        for i in range(len(arr) - 1):      # в случае равенства разниц - дополняю список 'ans'
            if arr[i + 1] - arr[i] < dif:  # возвращаю список
                dif = arr[i + 1] - arr[i]

        ans = []
        for i in range(len(arr) - 1):
            if arr[i + 1] - arr[i] == dif:
                ans.append((arr[i], arr[i + 1]))
        return ans