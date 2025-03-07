#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#


def gridChallenge(grid):
    # Write your code here
    sorted_grid = ["".join(sorted(row)) for row in grid]

    for j in range(len(sorted_grid[0])):
        for i in range(len(sorted_grid) - 1):
            if sorted_grid[i][j] > sorted_grid[i + 1][j]:
                return "NO"
    return "YES"