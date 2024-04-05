partida = True
posicoes = [' ', ' ', ' ' ,' ', ' ', ' ', ' ', ' ', ' ', ' ']
gg = ''
print(f'{posicoes[0]} | {posicoes[1]} | {posicoes[2]}')
print(f'{posicoes[3]} | {posicoes[4]} | {posicoes[5]}')
print(f'{posicoes[6]} | {posicoes[7]} | {posicoes[8]}')

while partida == True:
    if partida is not False:
        valor = int(input('Qual casa você jogador X gostaria de preencher? '))
        
        if posicoes[valor] == ' ':
            posicoes[valor] = 'X'
            print(f'{posicoes[0]} | {posicoes[1]} | {posicoes[2]}')
            print(f'{posicoes[3]} | {posicoes[4]} | {posicoes[5]}')
            print(f'{posicoes[6]} | {posicoes[7]} | {posicoes[8]}')
        else:
            print('Você perdeu sua vez!, digite uma casa vazia!')
        
        if  posicoes[0] == posicoes[1] == posicoes[2] == 'X' or posicoes[3] == posicoes[4] == posicoes[5] == 'X' or posicoes[6] == posicoes[7] == posicoes[8] == 'X' or posicoes[0] == posicoes[3] == posicoes[6] == 'X' or posicoes[1] == posicoes[4] == posicoes[7] == 'X' or posicoes[2] == posicoes[5] == posicoes[8] == 'X' or posicoes[0] == posicoes[4] == posicoes[8] == 'X' or posicoes[2] == posicoes[4] == posicoes[6] == 'X': 
            partida =  False
            gg = 'x'
            break

        valor2 = int(input('Qual casa você  jogador O gostaria de preencher? '))

        if posicoes[valor2] == ' ':
            posicoes[valor2] = 'O'
            print(f'{posicoes[0]} | {posicoes[1]} | {posicoes[2]}')
            print(f'{posicoes[3]} | {posicoes[4]} | {posicoes[5]}')
            print(f'{posicoes[6]} | {posicoes[7]} | {posicoes[8]}')
        else:
            print('Você perdeu sua vez!, digite uma casa vazia!')

        if  posicoes[0] == posicoes[1] == posicoes[2] == 'O' or posicoes[3] == posicoes[4] == posicoes[5] == 'O' or posicoes[6] == posicoes[7] == posicoes[8] == 'O' or posicoes[0] == posicoes[3] == posicoes[6] == 'O' or posicoes[1] == posicoes[4] == posicoes[7] == 'O' or posicoes[2] == posicoes[5] == posicoes[8] == 'O' or posicoes[0] == posicoes[4] == posicoes[8] == 'O' or posicoes[2] == posicoes[4] == posicoes[6] == 'O':
            partida  = False
            gg = '0'     

if gg == '0':
    print(f'Parabéns, O jogador de O venceu!')
elif gg == 'x':
    print(f'Parabéns, O jogador de X venceu!')