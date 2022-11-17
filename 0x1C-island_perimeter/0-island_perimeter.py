#!/usr/bin/python3
"""
island_perimiter
"""


def island_perimeter(grid):
    perimiter = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                perimiter += 4
                if i > 0 and grid[i - 1][j] == 1:
                    perimiter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimiter -= 2
    return perimiter
