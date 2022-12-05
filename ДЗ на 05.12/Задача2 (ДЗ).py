class Solution:                                # Сложность = O(n)
    def numberOfMatches(self, n: int) -> int:  # n: int - кол-во команд в турнире
        return n - 1                           # int: - кол-во матчей, который были сыграны до момента определения победителя