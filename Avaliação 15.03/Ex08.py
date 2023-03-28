#8 - Usando a função len() imprima em tela quantos caracteres cada item da lista gerada no exercício possui:

from Ex04 import lista

lista_convertida = ''

for n in range(10):
    lista_convertida += str(lista[n])

print(f'A sua lista possui {len(lista_convertida)} caracteres.')
