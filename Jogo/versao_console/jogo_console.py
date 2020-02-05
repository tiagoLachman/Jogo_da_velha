class Velha:
    def __init__(self):
        self._tabela = [_ for _ in range(9)]

    def posicionar_letra(self):
        pos = int(self._tabela.index(int(Velha.pegar_letra())))
        self._tabela[pos] = 'X'

    @staticmethod
    def iniciar(self):
        print("JOGO DA VELHA\nVERSAO 0.1\nSEMPRE DOIS JOGADORES\nR:")

    def pegar_letra():
        return input("Digite o número que corresponde a posição desejada:")


if __name__ == '__main__':
    jogo = Velha()
    print("Salve")
    print(jogo._tabela)
    jogo.posicionar_letra()
    print(jogo._tabela)
