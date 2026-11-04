def define_posicoes(linha, coluna, orientacao, tamanho): #tentei colocar uma estrutura usando o for, acho que agora vai funcionar :>
    posicoes = []

    if orientacao == "vertical":
        for i in range(tamanho):
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
 










def solicita_posicionamento(frota):
    embarcacoes = [
        ("porta-aviões", 5),
        ("navio-tanque", 4),
        ("contratorpedeiro", 3),
        ("submarino", 1)
    ]

    for nome_navio, tamanho in embarcacoes:
        while True:
            print(
                f"Insira as informações referentes ao navio {nome_navio} "
                f"que possui tamanho {tamanho}"
            )

            linha = int(input("Linha: "))
            coluna = int(input("Coluna: "))

            if nome_navio == "submarino":
                orientacao = "vertical"
            else:
                opcao = int(input("Orientação (1 para vertical, 2 para horizontal): "))

                if opcao == 1:
                    orientacao = "vertical"
                elif opcao == 2:
                    orientacao = "horizontal"
                else:
                    print("Esta posição não está válida!")
                    continue

            if posicao_valida(frota, linha, coluna, orientacao, tamanho):
                preenche_frota(
                    frota, nome_navio, linha, coluna, orientacao, tamanho
                )
                break

            print("Esta posição não está válida!")

    return frota

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
            while True:
                print(
                    f"Insira as informações referentes ao navio {nome_navio} "
                    f"que possui tamanho {tamanho}"
                )

                linha = int(input())
                coluna = int(input())

                if nome_navio == "submarino":
                    orientacao = "vertical"
                else:
                    opcao = int(input())

                    if opcao == 1:
                        orientacao = "vertical"
                    elif opcao == 2:
                        orientacao = "horizontal"
                    else:
                        print("Esta posição não está válida!")
                        continue

                if posicao_valida(
                    frota, linha, coluna, orientacao, tamanho
                ):
                    preenche_frota(
                        frota, nome_navio, linha, coluna, orientacao, tamanho
                    )
                    break

                print("Esta posição não está válida!")

    print(frota)


solicita_posicionamento()


frota_oponente = {
    "porta-aviões": [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    "navio-tanque": [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    "contratorpedeiro": [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    "submarino": [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

tabuleiro_oponente = posiciona_frota(frota_oponente)
tabuleiro_jogador = posiciona_frota(frota_jogador)

posicoes_informadas = set()
jogando = True

while jogando:
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))

    while True:
        linha = int(input())

        if 0 <= linha <= 9:
            break

        print("Linha inválida!")

    while True:
        coluna = int(input())

        if 0 <= coluna <= 9:
            break

        print("Coluna inválida!")

    if (linha, coluna) in posicoes_informadas:
        print(
            f"A posição linha {linha} e coluna {coluna} "
            "já foi informada anteriormente!"
        )
        continue

    posicoes_informadas.add((linha, coluna))
    tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha, coluna)

    if afundados(frota_oponente, tabuleiro_oponente) == 10:
        print("Parabéns! Você derrubou todos os navios do seu oponente!")
        jogando = False