# 9 - Crie uma lista contendo 5 nomes e adicione esta lista dentro da lista gerada no exercício 4

from Ex04 import lista

lista_nomes = []

for n in range(5):
    nome = input(f'Digite o {n+1}º nome: ')
    lista_nomes.append(nome)

lista.append(lista_nomes)

if __name__ == '__main__':
    print(lista)