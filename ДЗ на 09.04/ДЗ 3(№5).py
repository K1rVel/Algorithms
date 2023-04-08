# Сложность O(rows * columns)

def islandPerimeter(grid):
    x = len(grid)
    y = len(grid[0])

    perimeter = 0

    for i in range(x):
        for j in range(y):
            if grid[i][j] == 1:
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1
                if i == x - 1 or grid[i+1][j] == 0:
                    perimeter += 1
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1
                if j == y - 1 or grid[i][j+1] == 0:
                    perimeter += 1

    return