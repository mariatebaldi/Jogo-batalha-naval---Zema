def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []

    if orientacao == "vertical":
        posicoes.append([linha + i, coluna])
    elif orientacao == "horizontal":
        for i in range(tamanho):
            posicoes.append([linha, coluna + i])
    
    return posicoes

def preenche_frota(frota, nome_navio,linha, coluna, orientacao, tamanho):
    novo_navio = define_posicoes(linha, coluna, orientacao, tamanho)

    if nome_navio in frota: 
        frota[nome_navio].append(novo_navio)
    else:
        frota[novo_navio] = [novo_navio]

    return frota

def faz_jogada(tabuleiro,linha,coluna):
    if tabuleiro[linha][coluna] == 1:
        # if tabuleiro[linha] == 1 and tabuleiro[caluna] == 1
        tabuleiro[linha][coluna] = "X"

    else:
        tabuleiro[linha][coluna]  = "-"


    return tabuleiro