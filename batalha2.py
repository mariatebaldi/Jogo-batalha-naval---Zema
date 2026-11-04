
# def preenche_frota(frota):
#     frota{
#         "Corveta":[[2,1]], #considerei a corveta como um navio de 1 espaço apenas
#         "Submarino":[[7,4],[8,4]],
#         "Contratorpedeiro":[[5,2],[5,3],[5,4]],
#         "Couraçado":[[1,6],[2,6][3,6][4,6]],
#         "Porta-aviões":[[9,5][9,6][9,7][9,8][9,9]],
    }


# def define_posicoes(ponto_inicial,direcao,tamanho):
#     #guardando as variaveis em listas
#     x = ponto_inicial[0]
#     y = ponto_inicial[1]
#     posicoes = []

#     for i < range(tamanho): 
#         if direcao == "Horizontal" or direcao == "horizontal":
#             x = x + 1 
#         else:
#             y = y + 1

#     return (posicoes)

def define_posicoes(linha_inicial,coluna_inicial,direcao,tamanho):
    y = linha_inicial  
    x = coluna_inicial 
    posicoes = []
    i = 0 

    while i < tamanho:
        if direcao == "horizontal" or direcao == "Horizontal":
            posicoes = posicoes + [[y, x + i] ]
        elif direcao == "Vertical" or direcao == "vertical":
            posicoes = posicoes + [[y + i, x]]
        else:
           return []

        i = i + 1

    return posicoes

def preenche_frota(frota, nome_navio, linha_inicial, coluna_inicial, direcao, tamanho): #frota é a lista que ja guarda os navios, depois ele mostra as informaçoes do navio
    posicoes = define_posicoes(linha_inicial, coluna_inicial,direcao, tamanho)
    frota[nome_navio] = posicoes
    return frota
#basicamente a variavel posicoes usa a funçao anterior para realizar os calculos e apos isso é armazenada em frota 

        



    