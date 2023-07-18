#Importar palavras aleatórias
import random
from os import system, name

def limpa_tela():
    if name == 'nt':
        _= system('cls')
    else:
        _= system('clear')

def game():

    limpa_tela()
    print('\nBem-vinda ao jogo da forca!')
    print('\nAdvinhe a palavra abaixo:')

    palavras = ['Banana', 'Maça', 'Pera', 'Uva', 'Jabuticaba']

    palavra = random.choice(palavras)

    letras_descobertas = ['_' for letra in palavra]

    chances = 6

    letras_erradas = []

    #print(letras_descobertas, '\n Você tem : {} chances' .format(chances), '\n Tentativas incorretas {}' .format(letras_erradas))

    while chances > 0:
        print("".join(letras_descobertas))
        print('\nChances restantes:', chances)
        print('\nLetras erradas:', ''.join(letras_erradas))

        tentativa = input('\nDigite uma letra:').lower()

        if tentativa in palavra:
            index = 0

            for letra in palavra: #passando por cada letra dentro da palavra
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        else:
            chances -= 1
            letras_erradas.append(tentativa)

        if "_" not in letras_descobertas:
            print('\nVocê venceu, a palavra era:', palavra)
            break

    if "_" in letras_descobertas:
        print('\nVocê perdeu, a palavra era:', palavra)

if __name__ == '__main__':
    game()
    print('\nParabéns. Você está aprendendo programação em Python com a DSA. :)\n')