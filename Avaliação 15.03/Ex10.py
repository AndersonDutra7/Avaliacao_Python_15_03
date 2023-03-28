#10 - Crie um programa para remover tudo que não for do tipo inteiro da lista gerada no exercício 9.

from Ex09 import lista_nomes

print(f'Segue sua lista: {lista_nomes}')

for n in range(len(lista_nomes)):
    if not lista_nomes[n].isalpha():
        lista_nomes.pop[n]

print(f'Sua lista editada sem núemros ficou: \033[1;32m{lista_nomes}\033[0m.')