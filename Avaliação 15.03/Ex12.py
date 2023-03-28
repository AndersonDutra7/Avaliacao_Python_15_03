# 12 - Utilize a função criada no exercício anterior e mostre em tela a
# soma total de todos os valores de uma lista.

from Ex11 import lista_inteiros

qtd_itens = ''

while True:
    qtd_itens = input('Digite a quantidade de itens na lista: ')
    if qtd_itens.isnumeric():
        qtd_itens = int(qtd_itens)
        break
    else:
        print('Por favor, digite um número inteiro: ')
        pass

lista_ex_12 = (lista_inteiros(qtd_itens))

print(f'A soma dos valores na lista 12 é: \033[1;32m{sum(lista_ex_12)}\033[0m.')

print(lista_ex_12)