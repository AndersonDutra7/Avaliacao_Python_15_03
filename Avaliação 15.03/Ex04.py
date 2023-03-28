# 4 - Escreva um programa que gere uma lista com 10 números aleatórios entre 20 e 1580:(utilize a lib random)

from random import randint

lista = []

for n in range(10):
    lista.append(randint(20, 1580))

# if __name__ == '__main__':
print(f'A lista gerada foi: \033[1;32m{lista}\033[0m.')