import numpy as np
from classes import *


def check_equation(equation: []) -> bool:
    print(equation)
    if sum([c == '=' for c in equation]) != 1:
        return False

    eq_sign_index = equation.index('=')
    left = equation[:eq_sign_index]
    right = equation[eq_sign_index + 1:]

    operands = left[::2]
    operators = left[1::2]

    print("operators: {}, operands {}".format(operators, operands))


def solve(data: Data):
    eq_after_add = []
    eq_after_rem = []

    print("Add then remove")
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

    print("Remove then add")
    for i, term_rem in enumerate(data.terms):
        print("Term_rem: " + term_rem)
        eq_after_add = list(data.terms)
        for a in remove[term_rem]:
            eq_after_add[i] = a
            for j, term_add in enumerate(eq_after_add):
                eq_after_rem = list(eq_after_add)
                for r in add[term_add]:
                    eq_after_rem[j] = r
                    if check_equation(eq_after_rem):
                        return str(eq_after_rem)

    output = ""
    return output
