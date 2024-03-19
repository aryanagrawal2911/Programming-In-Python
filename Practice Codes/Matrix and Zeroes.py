'''
Given an 'N' x 'M' integer matrix, if an element is 0, set its entire row and column to 0's.
In particular, your task is to modify it in such a way that if a cell has a value 0 (matrix[i][j] == 0),
then all the cells of the ith row and jth column should be changed to 0.
You must do it in place.
'''


from math import *
from collections import *
from sys import *
from os import *
from typing import List


def setZeros(matrix: List[List[int]]) -> None:

    rows, cols = len(matrix), len(matrix[0])

    zerows, zerocols = set(), set()

    for i in range(rows):
        for j in range(cols):

            if matrix[i][j] == 0:
                zerows.add(i)
                zerocols.add(j)

    for i in range(rows):
        for j in range(cols):

            if (i in zerows) or (j in zerocols):

                matrix[i][j] = 0


if __name__ == "__main__":

    t = int(input())

    for i in range(t):

        n, m = map(int, input().strip().split())
        matrix = []

        for i in range(n):
            matrix.append(list(map(int, input().strip().split())))

        setZeros(matrix)

        for row in matrix:
            for el in row:
                print(el, end = " ")
            print()