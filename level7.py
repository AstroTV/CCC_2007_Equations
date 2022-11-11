import numpy as np
from classes import *


def is_operator(char):
    return str(char) in ["+", "-", "="]


def check_equation(equation: []) -> bool:
    if sum([c == '=' for c in equation]) != 1:
        return False

    eq_sign_index = equation.index('=')
    left = equation[:eq_sign_index]
    right = equation[eq_sign_index + 1:]

    terms_left = []
    terms_right = []

    i = 0
    while i < len(left):
        term = ""
        if is_operator(left[i]):
            if left[i] == "-":
                term = "-"
                i += 1
            else:
                i += 1
                continue

        while i < len(left) and left[i].isnumeric():
            term += left[i]
            i += 1
        if is_operator(term):
            # We do not support multiple operators e.g. 1 -- 1 = 2
            return False
        terms_left.append(term)

    i = 0
    while i < len(right):
        term = ""
        if is_operator(right[i]):
            if right[i] == "-":
                term = "-"
                i += 1
            else:
                i += 1
                continue

        while i < len(right) and right[i].isnumeric():
            term += right[i]
            i += 1

        if is_operator(term):
            # We do not support multiple operators e.g. 1 -- 1 = 2
            return False
        terms_right.append(term)

    sum_left = sum([int(term) for term in terms_left])
    sum_right = sum([int(term) for term in terms_right])

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
                        return "".join(eq_after_rem)

    for i, term_rem in enumerate(data.terms):
        eq_after_add = list(data.terms)
        for a in remove[term_rem]:
            eq_after_add[i] = a
            for j, term_add in enumerate(eq_after_add):
                eq_after_rem = list(eq_after_add)
                for r in add[term_add]:
                    eq_after_rem[j] = r
                    if check_equation(eq_after_rem):
                        return "".join(eq_after_rem)

    output = "ERROR"
    return output
