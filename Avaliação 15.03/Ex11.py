# 11- Utilizando os códigos criados na resolução dos exercícios anteriores,
# crie uma função que retorne uma lista de itens inteiros e que receba a quantidade de itens a serem
# gerados por parâmetro.

from random import randint

def lista_inteiros(qtd):
    lista = []
    for n in range(qtd):
        lista.append(randint(0, 1999))
    return lista

if __name__ == '__main__':
    while True:
        try:
            nome = input('Olá usuário!!! Qual o seu nome? ')
            itens = int(input(f'Muito bem {nome}, digite a quantidade de itens que queres gerar na lista: '))
            break
        except ValueError:
            print('\033[1;31mVALOR DIGITADO ERRADO, REPITA A OPERAÇÃO!!!\033[0m')

    print(f'{nome} , a sua lista ficou assim: \033[1;32m\n{lista_inteiros(itens)} \033[0m.')