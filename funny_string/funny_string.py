#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'funnyString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def funnyString(s):
    # Write your code here
    diff_original = [abs(ord(s[i]) - ord(s[i + 1])) for i in range(len(s) - 1)]
    reversed_s = s[::-1]
    diff_reversed = [abs(ord(reversed_s[i]) - ord(reversed_s[i + 1])) for i in range(len(reversed_s) - 1)]
    return "Funny" if diff_original == diff_reversed else "Not Funny"