class Solution:    # Сложность = O(n)
                   # jewels: str - камни, являющиеся драгоценностями
                   # stones: str -камни, имеющиеся у нас в наличии
                   # int: - кол_-во камней, имеющихся у нас в наличии

    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        total = 0
        for stone in stones:
            if stone in jewels:
                total += 1
        return total