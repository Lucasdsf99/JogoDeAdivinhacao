from random import randint
maquina = randint(0, 5) # faz o computador pensar
print('-=-' * 15)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 15)
numero = int(input('Em que número eu pensei? ')) # jogador tenta adivinhar
if numero == maquina:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'Errou! Na verdade eu pensei no numero {maquina} e não no {numero}!')
    