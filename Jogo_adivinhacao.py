import random
<<<<<<< HEAD
=======
import time
>>>>>>> Initial commit
print('*********************************')
print('Bem vindo ao jogo de Adivinhação!')
print('*********************************')

numero_secreto = random.randrange(1,101) # Essa função gera número aleatório. Round = Arredonda pro mais próximo.
<<<<<<< HEAD
total_tentativas = 3
=======
total_tentativas = 0
pontos = 100


print('Qual nível de dificuldade? ', numero_secreto)
print('(1) Fácil (2) Médio (3) Difícil')

nivel = int(input("Define um nível: "))

if nivel == 1:
    total_tentativas = 20
elif nivel == 2:
    total_tentativas = 10
else:
    total_tentativas = 5
>>>>>>> Initial commit

for rodada in range(1, total_tentativas + 1):
    print(f'Tentativas {rodada} de {total_tentativas}')
    chute_str = input('Digite um número entre 1 e 100: ')
    print(f"Você digitou {chute_str}")
    chute = int(chute_str) #Transforma um tipo string para um tipo inteiro.

    if chute < 1 or chute > 100:
        print('Você deve digitar um número  '' W entre 1 e 100!')
        continue #Volta pro laço de repetição

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
<<<<<<< HEAD
        print('Você acertou')
=======
        print(f'Você acertou e fez {pontos} pontos')
>>>>>>> Initial commit
        break #Não vai continuar rodando
    else:
        if(maior):
            print('Você errou. O seu chute foi maior que o número secreto!')
        elif(menor):
            print('Você errou. O seu chute foi menor que o número secreto!')
<<<<<<< HEAD
    print('Fim do Jogo')
print(numero_secreto)
=======
        pontos_perdidos = abs(pontos-(numero_secreto - chute)) #40-60. Incluido a função abs= número absoluto
        pontos = pontos - pontos_perdidos

print('Fim do Jogo')
print(f'O número correto era: {numero_secreto}')
time.sleep(5.5) # Pause 5.5 seconds
>>>>>>> Initial commit
