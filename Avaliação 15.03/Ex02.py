# 2 - Imprima as palavras que contenham letras e números juntos da frase abaixo:
#
frase = 'Paulo é d4veloper e um b0m musico'

for n in frase.split():
    if not n.isalpha():
        print(n)