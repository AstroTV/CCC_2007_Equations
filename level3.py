import numpy as np
from classes import *


def solve(data: Data):
    for t in transformations[data.left]:
        if t + data.right == data.solution:
            if data.right < 0:
                return "{}{}={}".format(t, data.right, data.solution)
            else:
                return "{}+{}={}".format(t, data.right, data.solution)

    for t in transformations[data.right]:
        if data.left + t == data.solution:
            if data.right < 0:
                return "{}{}={}".format(data.left, t, data.solution)
            else:
                return "{}+{}={}".format(data.left, t, data.solution)

    for a in add[data.left]:
        for r in remove[data.right]:
            if a + r == data.solution:
                if data.right < 0:
                    return "{}{}={}".format(a, r, data.solution)
                else:
                    return "{}+{}={}".format(a, r, data.solution)
        for r in remove[data.solution]:
            if a + data.right == r:
                if data.right < 0:
                    return "{}{}={}".format(a, data.right, r)
                else:
                    return "{}+{}={}".format(a, data.right, r)

    for a in add[data.right]:
        for r in remove[data.left]:
            if r + a == data.solution:
                if data.right < 0:
                    return "{}{}={}".format(r, a, data.solution)
                else:
                    return "{}+{}={}".format(r, a, data.solution)
        for r in remove[data.solution]:
            if data.left + a == r:
                if data.right < 0:
                    return "{}{}={}".format(data.left, a, r)
                else:
                    return "{}+{}={}".format(data.left, a, r)

    for a in add[data.solution]:
        for r in remove[data.left]:
            if r + data.right == a:
                if data.right < 0:
                    return "{}{}={}".format(r, data.right, a)
                else:
                    return "{}+{}={}".format(r, data.right, a)
        for r in remove[data.right]:
            if data.left + r == a:
                if data.right < 0:
                    return "{}{}={}".format(data.left, r, a)
                else:
                    return "{}+{}={}".format(data.left, r, a)

    print("ERROR: No solution found")
    return "ERROR"
