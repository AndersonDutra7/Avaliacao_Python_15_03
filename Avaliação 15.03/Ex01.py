# 1 - Remova strings vazias da lista de strings abaixo:
# lista_nomes = [‘Emanoela’, ‘Jonatan’, ‘’, ‘Kelly’, None, ‘Henrique’, ‘’]

# lista_nomes = ['Emanoela', 'Jonatan', '', 'Kelly', None, 'Henrique', '']
# lista_nomes = list(filter(None, lista_nomes))
# print(lista_nomes)


lista_nomes2 = ['Emanoela', 'Jonatan', '', 'Kelly', None, 'Henrique', '']

try:
    while True:
        lista_nomes2.remove("")
except ValueError:
    pass

print(lista_nomes2)