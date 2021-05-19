'''
    Solução para a avaliação A4 da disciplina INE5603 do semestre 2020.2.

    Author: Pedro Santi Binotto (20200634)
    Date created: 17/05/2021
    Date last modified: 19/05/2021 
    Python Version: 3.7.3
'''

from typing import Iterable


class CampoMinado:
    def __init__(self, matriz: Iterable[int]):
        self.__matriz_base = matriz
        self.__height = len(self.__matriz_base)
        self.__width = len(self.__matriz_base[0])
        self.__campo = self.__matriz_base.copy()
        self.__col = 3                                                          # Valor que será utilizado para formatar
                                                                                # a impressão das matrizes.
    def conta(self, m: Iterable[int], pos: Iterable[int]):
        height = self.__height
        width = self.__width
        cnt = 0
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if not (i == 0 and j == 0) and\
                    (-1 < pos[0] + i <= height - 1) and\
                    (-1 < pos[1] + j <= width - 1 ):
                    if m[pos[0] + i][pos[1] + j] == -1:
                        cnt += 1
        return cnt

    def computa_matriz(self):
        height = self.__height
        width = self.__width
        for i in range(height):
            for j in range(width):
                if self.__matriz_base[i][j] == 0:
                    self.__campo[i][j] = self.conta(self.__matriz_base, (i, j))

    def __str__(self):                                                          # TODO: Escrever baseado nas conidções 
        col = self.__col                                                        # artuas do jogo
        height = len(self.__campo)
        res = ""
        for i in range(height):
            res += "".join(str(j).rjust(col) for j in self.__campo[i])          # Justifica cada elemento em forma de
            res += '\n'                                                         # string para imprimir.
        return res
