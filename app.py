print('Start game')

tabuleiro = [
    ['_' , '_', '_'],
    ['_' , '_', '_'],
    ['_' , '_', '_']
]

tabuleiro_atual = tabuleiro

rodada = 0

jogador_atual = 'X'

def imprime_tabuleiro(tabuleiro):
    for i in range(3):
        for j in range(3):
            print(tabuleiro[i][j], end= ' ')
        print('')
        
def troca_jogador(jogador):
    if jogador == 'O':
        return 'X'
    else: 
        return 'O'

def verifica_vitoria(tabuleiro):
    print('Verificando vítoria')
    for i in range(3): 
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] and tabuleiro[0][i] != '_': return True
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] and tabuleiro[i][0] != '_': return True
    
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] and tabuleiro[0][0] != '_': return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] and tabuleiro[0][2] != '_': return True
    return False

while (True):    
    
    print(f'Turno { rodada + 1 }')
    
    print(f'Rodada do jogador: {jogador_atual}')
    
    imprime_tabuleiro(tabuleiro_atual)
    
    try:
        linha_jogada = int(input('Digite o número da linha desejada: ')) - 1
        coluna_jogada = int(input('Digite o número da coluna desejada: ')) - 1
        
        if linha_jogada not in [0, 1, 2] or coluna_jogada not in [0, 1, 2]:
            print("Jogada Inválida, fora dos limites, tente novamente!")
            continue
    except ValueError:
        print("Jogada Inválida, valor inválido, tente novamente!")
        continue
    
    if tabuleiro_atual[linha_jogada][coluna_jogada] != '_':
        print('Posição já ocupada')
        continue
    else:
        tabuleiro_atual[linha_jogada][coluna_jogada] = jogador_atual
    
    if verifica_vitoria(tabuleiro_atual):
        imprime_tabuleiro(tabuleiro_atual)
        print(f'Vencedor foi o jogador: {jogador_atual}')
        break
    
    jogador_atual = troca_jogador(jogador_atual)
    rodada += 1
    
    if rodada == 9:
        imprime_tabuleiro(tabuleiro_atual)
        print('Empate')
        break
    

    