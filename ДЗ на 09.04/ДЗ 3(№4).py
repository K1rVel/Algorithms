# Сложность O(mn)

def numIslands(grid):
    def dfs(g, p):
        if g < 0 or p < 0 or g >= m or p >= n or grid[g][p] == '0':
            return
        grid[g][p] = '0'
        dfs(g+1, p)
        dfs(g-1, p)
        dfs(g, p+1)
        dfs(g, p-1)

    m = len(grid)
    n = len(grid[0])
    count = 0

    for g in range(m):
        for p in range(n):
            if grid[g][p] == '1':
                count += 1
                dfs(g, p)

    return count