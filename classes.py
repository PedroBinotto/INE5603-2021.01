'''
    Solução para a avaliação A4 da disciplina INE5603 do semestre 2020.2.

    Author: Pedro Santi Binotto (20200634)
    Date created: 17/05/2021
    Date last modified: 20/05/2021 
    Python Version: 3.7.3
'''

import copy
import random
from typing import Iterable


class CampoMinado:
    def __init__(self, height, width, matriz: Iterable[int]=None):
        self.__height = height
        self.__width = width
        self.__matriz_base = matriz if matriz is not None\
            else self.__gerar_matriz()
        self.__campo = copy.deepcopy(self.__matriz_base)                        # Neste caso cópias 'shallow' não bastam
        self.__mapa_descoberta = self.__gerar_matriz(vazia=True)                # Matriz utilizada para mapear posições
        self.__col = 3                                                          # Valor que será utilizado para formatar
        self.__total_livre = 0                                                  #    a impressão das matrizes.
        self.__computa_matriz()

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
   
    def __gerar_matriz(self, vazia: bool=False):
        m = []
        height = self.__height
        width = self.__width
        for i in range(height):
            if vazia:
                m.append([0] * width)
            else:
                m.append(random.choices([0, -1], weights = [5, 1], k=width))
        return m

    def __computa_matriz(self):                                                 # Cria matriz do jogo à partir da
        height = self.__height                                                  #     matriz base.
        width = self.__width
        if height != len(self.__matriz_base)\
            or width != len(self.__matriz_base[0]):
            print('Dimensões incompatíveis com a matriz inserida!')
            quit()
        for i in range(height):
            for j in range(width):
                if self.__matriz_base[i][j] == 0:
                    self.__campo[i][j] = self.__conta(self.__matriz_base, (i, j))
                    self.__total_livre += 1

    def marca_pos(self, x: int, y: int):                                        # Marca posições descobertas na matriz
        height = self.__height                                                  #   'mapa_descoberta'.
        width = self.__width
        if (x > height or x < 0) or\
            (y > width or x < 0):
            print('Posição inválida!')
        elif self.__campo[x][y] == 0:
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
            self.__estado_jogo()
        elif self.__campo[x][y] != -1:
            self.__mapa_descoberta[x][y] = 1
            self.__estado_jogo()
        else:                                                                   # Caso o elemento selecionado seja -1.
            self.__mapa_descoberta[x][y] = 1
            self.__perdeu()
   
    def __esconde(self, i, j):                                                  # Determina se dado elemento deve ou não
        if self.__mapa_descoberta[i][j] == 1:                                   #    ser exibido.
            return str(self.__campo[i][j])
        else:
            return '-'
    
    def __estado_jogo(self):
        total = 0
        for i in range(self.__height):
            for j in range(self.__width):
                if self.__mapa_descoberta[i][j] == 1:
                    total += 1
        if total == self.__total_livre:
            self.__venceu()

    def __venceu(self):
        print(self.__str__())
        print('\nVocê venceu!\n')
        quit()

    def __perdeu(self):
        print(self.__str__())
        print('\nVocê perdeu!\n')
        quit()

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
