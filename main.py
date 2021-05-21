'''
    Solução para a avaliação A4 da disciplina INE5603 do semestre 2020.2.

    Author: Pedro Santi Binotto (20200634)
    Date created: 17/05/2021
    Date last modified: 20/05/2021 
    Python Version: 3.7.3
'''

from classes import CampoMinado


def main():
    print('[CampoMinado]')
    print('\nSeja bem vindo!')

    while True:
        try:
            linhas = int(input('\nInforme o número de linhas: '))
            colunas = int(input('Informe o número de colunas: '))
            break
        except ValueError:
            print('\nPor favor informe números inteiros.')

    while True:
        input_gerar = input('Gerar matriz de campo aleatoriamente?\n(s/n): ')
        if input_gerar.lower() in ['s', 'sim']:
            gerar = True
            break
        elif input_gerar.lower() in ['n', 'nao', 'não']:
            gerar = False
            break
        else:
            print('\nPor favor responda com "sim" ou "não"\n')
    
    if not gerar:
        matriz = []
        for i in range(linhas):
            print('''
Informe os elementos ({}) da linha {}, separados por espaços.\n\
Insira "0" para um espaço livre e "-1" para uma mina.'''\
            .format(colunas, i))
            while True:
                elem_string = input('\n$ ')
                try:
                    int_list = [int(j) for j in elem_string.split()]
                except ValueError:
                    print('Insira somente "0" e "-1"s.')
                    continue

                if len(int_list) == colunas:
                    flag = True
                    for j in int_list:
                        if j in [0, -1]:
                            pass
                        else:
                            flag = False
                            print('Insira somente "0" e "-1"s.')
                            break
                    matriz.append(int_list)
                else:
                    flag = False
                    print('Número de elementos não coincide com número de colunas.\n')
                if flag:
                    break
    else:
        matriz = None

    campo = CampoMinado(
        height=linhas,
        width=colunas,
        matriz=matriz
    )
    print('''\nJogo Iniciado! \n
A contagem de linhas e colunas é iniciada em "0", i.e, a primeira linha é de
 coordenada 0, a segunda, de coordenada 1, etc...\n''')
    print(campo.__str__())
    while True:
        try:
            i = int(input('Insira a coordenada "x":\n$ '))
            j = int(input('Insira a coordenada "y":\n$ '))
            if (i > linhas or i < 0) or\
                (j > colunas or j < 0):
                raise IndexError
            else:
                campo.marca_pos(i, j)
            print(campo.__str__(), '\n')
        except IndexError:
            print('\nValor inválido!\n')

main()
