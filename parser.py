import sys

def parseFile(file):
    matrix = []
    with open(file, 'r') as f:
        intel_list = []
        for row, line in enumerate(f):
            if row < 1:
                for column, word in enumerate(line.split()):
                    intel_list.insert(column, word)
                matrix = [[0 for x in range(int(intel_list[1]))] for y in range(int(intel_list[0]))]
            else :
                for column, char in enumerate(line):
                    if column < int(intel_list[1]) :
                        matrix[row - 1][column] = char
    return matrix, intel_list[2], intel_list[3]
