#!/usr/bin/python3
"""
island_perimiter
"""


def island_perifiermeter(grid):
    perifier = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                perifier += 4
                if i > 0 and grid[i - 1][j] == 1:
                    perifier -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perifier -= 2
    return perifier