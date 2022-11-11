import os
from pprint import pprint
import sys

import level1
import level2
import level3
import level4
import level5
import level6
import level7
from classes import *


def load(input_data):
    terms = [*input_data]

    return Data(terms=terms)


if __name__ == "__main__":
    level, quests = 7, 1
    input_eqs = ["93+27-30+16=68", "78+23-89+82=94+2-18"]
    for q in range(0, quests + 1):

        fileextension = '/level{0}/level{0}_{1}.in'.format(level, q)
        input_file = os.getcwd() + fileextension
        output_file = os.path.splitext(input_file)[0] + ".out"

        data = load(input_eqs[q])
        pprint(data)

        print("=== Input {}".format(q))
        print("======================")

        if level == 1:
            result = level1.solve(data)
        elif level == 2:
            result = level2.solve(data)
        elif level == 3:
            result = level3.solve(data)
        elif level == 4:
            result = level4.solve(data)
        elif level == 5:
            result = level5.solve(data)
        elif level == 6:
            result = level6.solve(data)
        elif level == 7:
            result = level7.solve(data)

        pprint(result)

        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        with open(output_file, 'w+') as fo:
            fo.write(result)
