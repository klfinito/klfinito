def mostra_tabuleiro(tabuleiro):
    print("  1   2   3")
    coluna = ["A", "B", "C"]
    o = 0
    linhas = []
    for x in tabuleiro:
        linhas = linhas + [coluna[o] + " " + x[0] + " | " + x[1] + " | " + x[2] + " "]
        linhas = linhas + [" ---|---|---"]
        o = o + 1
    linhas = linhas[:-1]
    for x in linhas:
        print(x)

def regista_jogada(tabuleiro, simbolo, posicao):
    linha = tabuleiro[posicao[1]]
    linha = list(linha)
    linha[posicao[0]] = simbolo
    linha = "".join(linha)
    tabuleiro[posicao[1]] = linha
    return tabuleiro

def vitoria(tabuleiro):
    vitorias = [
        tabuleiro[0],
        tabuleiro[1],
        tabuleiro[2],
        [tabuleiro[0][0], tabuleiro[1][0], tabuleiro[2][0]],
        [tabuleiro[0][1], tabuleiro[1][1], tabuleiro[2][1]],
        [tabuleiro[0][2], tabuleiro[1][2], tabuleiro[2][2]],
        [tabuleiro[0][0], tabuleiro[1][1], tabuleiro[2][2]],
        [tabuleiro[0][2], tabuleiro[1][1], tabuleiro[2][0]],
    ]
    for n in vitorias:
        if n != [" ", " ", " "]:
            if len( set( n ) ) == 1:
                print("win")
                main()
        else:
            pass

def tie(tabuleiro):
    if " " not in tabuleiro:
        print("tie")

def main():
    tabuleiro = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    mostra_tabuleiro(tabuleiro)

    simbolo = "X"
    while True:
        posicao_jogador = input("Posicao: ")
        posicao_jogador = posicao_jogador.upper()
        x = int(posicao_jogador[1]) - 1
        if posicao_jogador[0] == "A":
            y = 0
        elif posicao_jogador[0] == "B":
            y = 1
        elif posicao_jogador[0] == "C":
            y = 2

        tabuleiro = regista_jogada(tabuleiro, simbolo, [x, y])

        mostra_tabuleiro(tabuleiro)

        if simbolo == "X":
            simbolo = "O"
        elif simbolo == "O":
            simbolo = "X"

        vitoria(tabuleiro)

        tie(tabuleiro)
main()
