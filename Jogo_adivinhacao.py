import random
print('*********************************')
print('Bem vindo ao jogo de Adivinhação!')
print('*********************************')

numero_secreto = random.randrange(1,101) # Essa função gera número aleatório. Round = Arredonda pro mais próximo.
total_tentativas = 3

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
        print('Você acertou')
        break #Não vai continuar rodando
    else:
        if(maior):
            print('Você errou. O seu chute foi maior que o número secreto!')
        elif(menor):
            print('Você errou. O seu chute foi menor que o número secreto!')
    print('Fim do Jogo')
print(numero_secreto)