print('Bem-vinda a calculadora básica da Emily Saucedo')

def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def multipl(x,y):
    return x*y
def divide(x,y):
    return x/y

opdef = input(str('Selecione qual a operação desejada: (Soma/Subtração/Multiplicação/Divisão)'))
op = opdef.lower()

if op == 'soma' or op == 'subtração' or op == 'multiplicação' or op == 'divisão':
    print("A operação selecionada foi: {}" .format(op))
    contador = int(input('Com quantos números será feita a operação?'))

    num1 = float(input('Digite o primeiro número da operaçao:'))
    num2 = float(input('Digite o segundo número da operaçao:'))

    if op == 'soma':
        print('A soma dos valores é: {}'.format(add(num1,num2)))
        print(num1, '+', num2, '=', add(num1,num2))
    elif op == 'subtração':
        print('A subtração dos valor 1 menos o 2 é: {}'.format(sub(num1, num2)))
        print('A subtração dos valor 2 menos o 1 é: {}'.format(sub(num2, num1)))
    elif op == 'multiplicação':
        print('A multplicação é: {}'.format(multipl(num1,num2)))
    elif op == 'divisão':
        if num2 == 0:
            print('Não existe divisão por zero! ERRO!')
        else:
            print('A divisao resulta em: {}'.format(divide(num1,num2)))

else:
    print('Operação inválida!')

