import numpy as np
from classes import *

transformations = {}


def solve(data: Data):
    if data.left == data.right:
        return "{}={}".format(data.left, data.right)

    # Try to fix left
    for t in transformations[data.left]:
        if t == data.right:
            return "{}={}".format(t, data.right)

    # Try to fix right
    for t in transformations[data.right]:
        if t == data.left:
            return "{}={}".format(data.left, t)

    print("ERROR: No solution found")
    return "ERROR"
