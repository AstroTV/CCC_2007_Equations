from dataclasses import dataclass


# from collections import namedtuple


# Task = namedtuple('Task', ['id', 'powerdemand','startint', 'endint'])


@dataclass
class Data:
    terms: [str]


class Number:
    def __init__(self, number):
        self.number = number


'''
transformations = {0: [6, 9], 1: [], 2: [3], 3: [2, 5], 4: [], 5: [3], 6: [0, 9], 7: [], 8: [], 9: [0, 6], -0: [-6, -9],
                   -1: [], -2: [-3], -3: [-2, -5], -4: [], -5: [-3], -6: [-0, -9], -7: [], -8: [], -9: [-0, -6]}
remove = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [5], 7: [1], 8: [0, 6, 9], 9: [3, 5], -0: [], -1: [], -2: [],
          -3: [], -4: [], -5: [], -6: [-5], -7: [-1], -8: [-0, -6, -9], -9: [-3, -5]}
add = {0: [8], 1: [7], 2: [], 3: [9], 4: [], 5: [6, 9], 6: [8], 7: [], 8: [], 9: [8], -0: [-8], -1: [-7], -2: [],
       -3: [-9], -4: [], -5: [-6, -9], -6: [-8], -7: [], -8: [], -9: [-8]}
'''

remove = {'0': [], '1': [], '2': [], '3': [], '4': [], '5': [], '6': ['5'], '7': ['1'], '8': ['0', '6', '9'],
          '9': ['3', '5'], '+': ['-'], '-': [], '=': ['-']}

add = {'0': ['8'], '1': ['7'], '2': [], '3': ['9'], '4': [], '5': ['6', '9'], '6': ['8'], '7': [], '8': [], '9': ['8'],
       '+': [], '-': ['+', '='], '=': []}