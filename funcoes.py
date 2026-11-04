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
        frota[nome_navio] = [novo_navio]

    return frota

def faz_jogada(tabuleiro,linha,coluna):
    if tabuleiro[linha][coluna] == 1:
        # if tabuleiro[linha] == 1 and tabuleiro[caluna] == 1
        tabuleiro[linha][coluna] = "X"

    else:
        tabuleiro[linha][coluna]  = "-"


    return tabuleiro


def posiciona_frota(frota):
    tabuleiro = [[0]*10 for _ in range(10)]

    for nome_navio in frota:
        for posicao in frota[nome_navio]:
            linha = posicao[0]
            coluna = posicao[1]
            tabuleiro[linha][coluna] = 1


    return tabuleiro


def afundados(frota,tabuleiro): #para um navio ser afundado ele deve ter todos os seu componentes escolhidos

    navios_afundados =  0  #quantidade de navios afundados no inicio          

    for nome_navio in frota:
        for posicoes_navio in frota[nome_navio]:  #armazeno e verifico se os elementos do navio possuem x para saber se foram afundados
            navio_afundado = True

            for posicao in posicoes_navio:
                linha = posicao[0]
                coluna = posicao[1]

                if tabuleiro[linha][coluna] != "X":
                    navio_afundado = False

            if navio_afundado:
                navios_afundados = navios_afundados + 1

    
    return navios_afundados
