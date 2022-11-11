import numpy as np
from classes import *


def solve(data: Data):
    possible_left = {data.left + data.right: "{}+{}".format(data.left, data.right)}
    possible_right = {data.solution: "{}".format(data.solution)}
    for t in transformations[data.left]:
        possible_left[t + data.right] = "{}+{}".format(t, data.right)
    for t in transformations[data.right]:
        possible_left[data.left + t] = "{}+{}".format(data.left, t)
    for t in transformations[data.solution]:
        possible_right[t] = "{}".format(t)

    for i in possible_left.keys():
        for j in possible_right.keys():
            if i == j:
                return "{}={}".format(possible_left[i], possible_right[j])

    print("ERROR: No solution found")
    return "ERROR"
