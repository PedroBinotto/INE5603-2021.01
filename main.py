'''
    Solução para a avaliação A4 da disciplina INE5603 do semestre 2020.2.

    Author: Pedro Santi Binotto (20200634)
    Date created: 17/05/2021
    Date last modified: 19/05/2021 
    Python Version: 3.7.3
'''

from classes import CampoMinado


def main():
    matriz = [
        [ 0,  -1,  0,  0, -1,  0,  0],
        [ 0,  -1,  0,  0, -1,  0,  0],
        [ 0,   0,  0,  0,  0,  0,  0],
        [ 1,   0,  0, -1,  0,  0, -1],
        [ 0,   0,  0,  0,  0,  0, -1],
        [ 0,  -1,  0,  0,  0,  0, -1],
        [ 0,  -1,  0,  0,  0,  0,  0],
        [ 0,  -1,  0,  0,  0,  0,  0],
        [ 0,   0,  0,  0,  0,  0,  0],
        [ 1,  -1,  0, -1, -1,  0,  0]
    ]

    teste = [
        [1, 2, 3],
        [4, 0, 5],
        [6, 7, 8]
    ]

    campo = CampoMinado(matriz)
    campo.computa_matriz()
    print(campo.__str__())

main()
