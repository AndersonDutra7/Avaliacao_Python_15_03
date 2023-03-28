#6 - Crie um programa que use uma iteração para exibir elementos da lista gerada no exercício 4 presentes em posições de índice ímpares:

from Ex04 import lista

for n in range(10):
    if n == 0:
        print('Considerando apenas os índices ÍMPARES da lista, temos:')
    if (n % 2) == 0:
       pass
    else:
       print(f'O índice ímpar {n} da lista possui o número {lista[n]}.')
