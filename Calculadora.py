print('Bem-vinda a calculadora básica da Emily Saucedo')

opdef = input(str('Selecione qual a operação desejada: (Soma/Subtração/Multiplicação/Divisão)'))
op = opdef.lower()

if op == 'soma' or op == 'subtração' or op == 'multiplicação' or op == 'divisão':
    print("A operação selecionada foi: {}" .format(op))
    contador = int(input('Com quantos números será feita a operação?'))

    num1 = float(input('Digite o primeiro número da operaçao:'))
    num2 = float(input('Digite o segundo número da operaçao:'))

    if op == 'soma':
        result = num1 + num2
        print('A soma dos valores é: {}'.format(result))
        print(num1, '+', num2, '=', result)
    elif op == 'subtração':
        result1 = num1 - num2
        result2 = num2 - num1
        print('A subtração dos valor 1 menos o 2 é: {}'.format(result1))
        print('A subtração dos valor 2 menos o 1 é: {}'.format(result2))
    elif op == 'multiplicação':
        result = num1 * num2
        print('A multplicação é: {}'.format(result))
    elif op == 'divisão':
        if num2 == 0:
            print('Não existe divisão por zero! ERRO!')
        else:
            result = num1 / num2
            print('A divisao resulta em: {}'.format(result))

else:
    print('Operação inválida!')

