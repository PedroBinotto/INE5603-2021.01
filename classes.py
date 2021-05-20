'''
    Solução para a avaliação A4 da disciplina INE5603 do semestre 2020.2.

    Author: Pedro Santi Binotto (20200634)
    Date created: 17/05/2021
    Date last modified: 20/05/2021 
    Python Version: 3.7.3
'''

from typing import Iterable


class CampoMinado:
    def __init__(self, matriz: Iterable[int]):
        self.__matriz_base = matriz
        self.__height = len(self.__matriz_base)
        self.__width = len(self.__matriz_base[0])
        self.__campo = self.__matriz_base.copy()
        self.__mapa_descoberta = self.__cria_matriz(                            # Matriz utilizada para mapear posições
            self.__height,                                                      #    já descobertas.
            self.__width,                                                       #    Elementos inicializados para 0s.
            0
        )
        self.__col = 3                                                          # Valor que será utilizado para formatar
        self.__computa_matriz()                                                 #    a impressão das matrizes.

    def __conta(self, m: Iterable[int], pos: Iterable[int]):
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
    
    def __cria_matriz(self, h, w, val):
        m = []
        for i in range(h):
            m.append([val] * w)
        return m

    def __computa_matriz(self):                                                 # Cria matriz do jogo à partir da
        height = self.__height                                                  #     matriz base.
        width = self.__width
        for i in range(height):
            for j in range(width):
                if self.__matriz_base[i][j] == 0:
                    self.__campo[i][j] = self.__conta(
                        self.__matriz_base, (i, j)
                    )

    def marca_pos(self, x: int, y: int):                                        # Marca posições descobertas na matriz
        height = self.__height                                                  #   'mapa_descoberta'.
        width = self.__width
        if self.__campo[x][y] == 0:
            self.__mapa_descoberta[x][y] = 1
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    if not (i == 0 and j == 0) and\
                        (-1 < x + i <= height - 1) and\
                        (-1 < y + j <= width - 1 ):
                        if self.__campo[x + i][y + j] == 0 and\
                            not self.__mapa_descoberta[x + i][y + j] == 1:
                            self.marca_pos(x + i, y + j)
                        elif self.__campo[x + i][y + j] != -1:
                            self.__mapa_descoberta[x + i][y + j] = 1
        elif self.__campo[x][y] != -1:
            self.__mapa_descoberta[x][y] = 1
        else:
            self.__mapa_descoberta[x][y] = 1
            return False
   
    def __esconde(self, i, j):                                                  # Determina se dado elemento deve ou não
        if self.__mapa_descoberta[i][j] == 1:                                   #    ser exibido.
            return str(self.__campo[i][j])
        else:
            return '-'

    def __str__(self):
        col = self.__col
        height = self.__height
        width = self.__width
        res = ""
        for i in range(height):
            for j in range(width):
                res += "".join(self.__esconde(i, j).rjust(col))                 # Justifica cada elemento em forma de
            res += '\n'                                                         #    string para imprimir.
        return res
