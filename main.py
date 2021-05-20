'''
    Solução para a avaliação A4 da disciplina INE5603 do semestre 2020.2.

    Author: Pedro Santi Binotto (20200634)
    Date created: 17/05/2021
    Date last modified: 20/05/2021 
    Python Version: 3.7.3
'''

from classes import CampoMinado


def main():
    # matriz = [
    #     [ 0,  -1,  0,  0, -1,  0,  0],
    #     [ 0,  -1,  0,  0, -1,  0,  0],
    #     [ 0,   0,  0,  0,  0,  0,  0],
    #     [ 0,   0,  0, -1,  0,  0, -1],
    #     [ 0,   0,  0,  0,  0,  0, -1],
    #     [ 0,  -1,  0,  0,  0,  0, -1],
    #     [ 0,  -1,  0,  0,  0,  0,  0],
    #     [ 0,  -1,  0,  0,  0,  0,  0],
    #     [ 0,  -1,  0,  0,  0,  0,  0],
    #     [ 0,   0,  0, -1, -1,  0,  0]
    # ]

    print('')
    linhas = int(input('Insira o número de linhas para o campo: '))
    colunas = int(input('Insira o número de colunas para o campo: '))

    matriz = []
    for i in range(linhas):

    campo = CampoMinado(matriz)

    print(campo.marca_pos(7, 3))
    print(campo.__str__())

    print(campo.marca_pos(9, 0))
    print(campo.__str__())

    print(campo.marca_pos(8, 1))
    print(campo.__str__())

main()
