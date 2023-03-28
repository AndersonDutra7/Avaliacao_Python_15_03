#3 - Imprima os 10 primeiros números naturais após um número inserido no console usando um loop while:

while True:
    try:
        numero = int(input('Digite um numero NATURAL: '))
        if type(numero) != int:
            print('O valor digitado não é válido! Repita a operação...')
        elif numero < 0:
            print('O número digitado não é NATURAL! Repita a operação...')
        else:
            for numero in range(numero,numero + 10):
                print(numero+1)
            break
    except:
        print('O valor digitado não é válido! Repita a operação...')