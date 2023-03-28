#13 - Utilizando a função do exercício 11, imprima todos os números da lista como uma única string.

from Ex11 import lista_inteiros

qtd_itens = ''
lista_string = ''

while True:
    qtd_itens = input('Digite a quantidade de itens na lista: ')
    if qtd_itens.isnumeric():
        qtd_itens = int(qtd_itens)
        break
    else:
        print('\033[1;31mPor favor, digite um número inteiro: \033[0m')
        pass

lista_ex_13 = lista_inteiros(qtd_itens)
for n in range(len(lista_ex_13)):
    lista_string += str(lista_ex_13[n])

print(f'A lista 13 em forma de String é: \033[1;32m{lista_string}\033[0m.')

print(lista_ex_13)