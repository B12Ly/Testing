#!/bin/python3

import math
import os
import random
import re
import sys


def alternate(s):
    unique_chars = list(set(s))
    max_length = 0

    # สร้างคู่ตัวอักษรทั้งหมดที่เป็นไปได้
    for i in range(len(unique_chars)):
        for j in range(i + 1, len(unique_chars)):
            c1 = unique_chars[i]
            c2 = unique_chars[j]

            # สร้างสตริงที่เหลือเพียง c1 และ c2
            filtered = []
            for char in s:
                if char == c1 or char == c2:
                    filtered.append(char)

            # ตรวจสอบว่าสตริงสลับกันได้
            valid = True
            for k in range(1, len(filtered)):
                if filtered[k] == filtered[k - 1]:
                    valid = False
                    break

            if valid:
                current_length = len(filtered)
                if current_length > max_length:
                    max_length = current_length

    return max_length if max_length >= 2 else 0