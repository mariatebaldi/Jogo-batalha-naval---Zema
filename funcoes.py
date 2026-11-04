def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []

    for i in range(tamanho):
        if orientacao == "vertical":
            posicoes.append([linha + i, coluna])
        elif orientacao == "horizontal":
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
        for navio in frota[nome_navio]:
            for posicao in navio:
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



def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    novas_posicoes = define_posicoes(linha, coluna, orientacao, tamanho)

    
    for linha_pos, coluna_pos in novas_posicoes:  #nao adianta eu usar as variaveis da funcao para determinar os limites fo tabuleiro 
        if not (0 <= linha_pos < 10 and 0 <= coluna_pos < 10): #crio novas incognitas para isso
            return False

    
    posicoes_ocupadas = []

    for navios in frota.values():   #nao sei se da pra usar outra forma sem o values, pesquisei agora e achei mais facil desse jeito, dps tu olha ai oq vc acha malu 
        for posicoes_navio in navios:
            for posicao in posicoes_navio:
                posicoes_ocupadas.append(posicao)

    
    for posicao in novas_posicoes:
        if posicao in posicoes_ocupadas:
            return False

    return True  


def solicita_posicionamento():
    frota = {}

    embarcacoes = [
        ("porta-aviões", 1, 4),
        ("navio-tanque", 2, 3),
        ("contratorpedeiro", 3, 2),
        ("submarino", 4, 1)
    ]

    for nome_navio, quantidade, tamanho in embarcacoes:
        for _ in range(quantidade):
            posicionado = False

            while not posicionado:
                print(
                    f"Insira as informações referentes ao navio {nome_navio} "
                    f"que possui tamanho {tamanho}"
                )

                linha = int(input("Linha: "))
                coluna = int(input("Coluna: "))
                orientacao = ""

                if nome_navio == "submarino":
                    orientacao = "vertical"
                else:
                    opcao = int(input("Orientação: [1] Vertical [2] Horizontal "))

                    if opcao == 1:
                        orientacao = "vertical"
                    elif opcao == 2:
                        orientacao = "horizontal"

                if orientacao != "" and posicao_valida(frota, linha, coluna, orientacao, tamanho):
                    preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho)
                    posicionado = True
                else:
                    print("Esta posição não está válida!")

    return frota