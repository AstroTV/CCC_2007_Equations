import numpy as np
from classes import *


def solve(data: Data):
    for i in range(len(data.left)):
        for t_add in add[data.left[i]]:
            for j in range(len(data.left)):
                if i != j:
                    for t_rem in remove[data.left[j]]:
                        if sum(data.left) + t_add + t_rem - data.left[i] - data.left[j] == sum(data.right):
                            data.left[i] = t_add
                            data.left[j] = t_rem
                            return str(data.left) + "=" + str(data.right)

            for j in range(len(data.right)):
                for t_rem in remove[data.right[j]]:
                    if sum(data.left) + t_add - data.left[i] == sum(data.right) + t_rem - data.right[j]:
                        data.left[i] = t_add
                        data.right[j] = t_rem
                        return str(data.left) + "=" + str(data.right)

    for i in range(len(data.left)):
        for t in transformations[data.left[i]]:
            if sum(data.left) + t - data.left[i] == sum(data.right):
                data.left[i] = t
                return str(data.left) + "=" + str(data.right)

    temp = data.left
    data.left = data.right
    data.right = temp

    for i in range(len(data.left)):
        for t_add in add[data.left[i]]:
            for j in range(len(data.left)):
                if i != j:
                    for t_rem in remove[data.left[j]]:
                        if sum(data.left) + t_add + t_rem - data.left[i] - data.left[j] == sum(data.right):
                            data.left[i] = t_add
                            data.left[j] = t_rem
                            return str(data.left) + "=" + str(data.right)

            for j in range(len(data.right)):
                for t_rem in remove[data.right[j]]:
                    if sum(data.left) + t_add - data.left[i] == sum(data.right) + t_rem - data.right[j]:
                        data.left[i] = t_add
                        data.right[j] = t_rem
                        return str(data.left) + "=" + str(data.right)

    for i in range(len(data.left)):
        for t in transformations[data.left[i]]:
            if sum(data.left) + t - data.left[i] == sum(data.right):
                data.left[i] = t
                return str(data.left) + "=" + str(data.right)

    print("ERROR: No solution found")
    return "ERROR"
