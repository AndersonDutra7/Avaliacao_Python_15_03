# 14- Utilizando a função do exercício 11, crie uma lista,
# adicione a ela uma lista contendo 5 nomes e imprima todos os dados da lista como uma única string.

from Ex11 import lista_inteiros

while True:
    qtd_itens = input('Digite a quantidade de itens na lista: ')
    if qtd_itens.isnumeric():
        qtd_itens = int(qtd_itens)
        break
    else:
        print('Por favor, digite um número inteiro: ')
        pass

lista_ex_14 = lista_inteiros(qtd_itens)
lista_string14 = ''
cont = 0

while cont < 5:
    nome = (str(input(f'Digite o {cont+1}º nome: ')))
    if nome.isnumeric():
        print('\033[1;31mPor favor, digite um nome válido! \033[0m')
        pass
    else:
     lista_ex_14.append(nome)
     cont +=1

for n in range(len(lista_ex_14)):
    lista_string14 += str(lista_ex_14[n])

print(f'A lista 13 em forma de String é: \033[1;32m{lista_string14}\033[0m.')

print(lista_ex_14)