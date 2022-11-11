import numpy as np
from classes import *


def check_equation(equation: []) -> bool:
    if sum([c == '=' for c in equation]) != 1:
        return False

    eq_sign_index = equation.index('=')
    left = equation[:eq_sign_index]
    right = equation[eq_sign_index + 1:]

    sum_left = int(left[0]) if left[0].isdecimal() else 0
    sum_right = int(right[0]) if right[0].isdecimal() else 0

    for i, term in enumerate(left):
        if term == '-':
            sum_left -= int(left[i+1])
        elif term == '+':
            sum_left += int(left[i+1])

    for i, term in enumerate(right):
        if term == '-':
            sum_right -= int(right[i+1])
        elif term == '+':
            sum_right += int(right[i+1])

    return sum_left == sum_right


def solve(data: Data):
    eq_after_add = []
    eq_after_rem = []

    for i, term_add in enumerate(data.terms):
        eq_after_add = list(data.terms)
        for a in add[term_add]:
            eq_after_add[i] = a
            for j, term_rem in enumerate(eq_after_add):
                eq_after_rem = list(eq_after_add)
                for r in remove[term_rem]:
                    eq_after_rem[j] = r
                    if check_equation(eq_after_rem):
                        return str(eq_after_rem)

    for i, term_rem in enumerate(data.terms):
        eq_after_add = list(data.terms)
        for a in remove[term_rem]:
            eq_after_add[i] = a
            for j, term_add in enumerate(eq_after_add):
                eq_after_rem = list(eq_after_add)
                for r in add[term_add]:
                    eq_after_rem[j] = r
                    if check_equation(eq_after_rem):
                        return str(eq_after_rem)

    output = "ERROR"
    return output
