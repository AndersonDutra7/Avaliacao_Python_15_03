# 5 - Escreva um programa para exibir apenas os números da lista gerada no exercício 4
# que satisfaçam as seguintes condições:
#     -O número deve ser divisível por cinco
#     -Se o número for maior que 95 e menor que 150, pule-o e passe para o próximo número
#     -Se o número for maior que 1500, pare o loop

from Ex04 import lista

lista_ex_05 = []

for n in lista:
    if n > 1500:
        break
    elif n % 5 == 0:
        if n > 95 and n < 150:
            continue
        lista_ex_05.append(n)

print(f'Já a lista editada ficou: \033[1;32m{lista_ex_05}\033[0m.')