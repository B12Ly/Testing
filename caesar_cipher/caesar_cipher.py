#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#


def caesarCipher(s, k):
    # Write your code here
    effective_k = k % 26
    encrypted = []
    for char in s:
        if char.isupper():

            shifted = ord("A") + (ord(char) - ord("A") + effective_k) % 26
            encrypted.append(chr(shifted))
        elif char.islower():

            shifted = ord("a") + (ord(char) - ord("a") + effective_k) % 26
            encrypted.append(chr(shifted))
        else:

            encrypted.append(char)
    return "".join(encrypted)