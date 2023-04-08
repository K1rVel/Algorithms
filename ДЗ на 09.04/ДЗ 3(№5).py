# Сложность O(rows * columns)

def islandPerimeter(grid):
    x = len(grid)
    y = len(grid[0])

    perimetr = 0

    for g in range(x):
        for p in range(y):
            if grid[g][p] == 1:
                if g == 0 or grid[g-1][p] == 0:
                    perimetr += 1
                if g == x - 1 or grid[g+1][p] == 0:
                    perimetr += 1
                if p == 0 or grid[g][p-1] == 0:
                    perimetr += 1
                if p == y - 1 or grid[g][p+1] == 0:
                    perimetr += 1

    return perimetr