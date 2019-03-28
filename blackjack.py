import random


class Baralho(object):
    """
        Cria um baralho e distribui as cartas
    """
    def __init__(self):
        self.naipe = ('copas', 'espadas', 'ouro', 'paus')
        self.valor = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
        self.pontuacao = 0
        self.pontuacao_cpu = 0
        self.result = 0

    def embaralha_cartas(self):
        carta_sorteada = (self.naipe[random.randint(0, 3)], self.valor[random.randint(0, 12)])
        return carta_sorteada

    @staticmethod
    def pesquise(lista, ganho):
        for x, e in enumerate(lista):
            if e == ganho:
                return True
        return False

    @staticmethod
    def todas_cartas():
        bar = Baralho()
        todas = []
        while len(todas) < 52:
            sorteada = bar.embaralha_cartas()
            repetida = bar.pesquise(todas, sorteada)
            if not repetida:
                todas.append(sorteada)
        return todas

    @staticmethod
    def pega_carta(lista):
        uma_carta = lista[0]
        lista.remove(uma_carta)
        return uma_carta

    def soma_cartas(self, tupla):
        valor_dado = tupla[1]
        if valor_dado == 'Q' or valor_dado == 'J' or valor_dado == 'K':
            self.pontuacao += 10
        else:
            self.pontuacao += int(valor_dado)

    def guarda_resultado(self, result):
        self.result = result


class CPU(object):
    def __init__(self, lista):
        self.cartas = lista
        pass

    def jogada(self, apostar):
        t = 0
        inicio.pega_carta(self.cartas)
        print()
        print("________________________________________________")
        print("Vez da CPU")
        print()
        while len(cartas) >= 1:
            if t < 2:
                print(cartas[0])
                inicio.soma_cartas(inicio.pega_carta(cartas))
                t += 1
            else:
                if inicio.pontuacao > 21:
                    print("Voce ganhou, A casa estourou a pontuação")
                    apostar.mais(valor)

                    print("Pontuação da CPU é de: ", inicio.pontuacao)
                    break
                else:
                    print("Pontuação da CPU é de: ", inicio.pontuacao)

                    if inicio.pontuacao <= inicio.result:
                        t = 1
                    else:
                        print("Voce perdeu, A casa fez uma pontuação melhor")
                        
                        break


class Aposta(object):
    caixa = 10000
    def __init__(self):
        if self.caixa <= 0:
            print("Fim de jogo")
        else:
            print("Seu caixa é de: ", self.caixa)

    def mais(self, valor1):
        self.caixa += valor1

    def menos(self, valor2):
        self.caixa -= valor2

apostar = Aposta()
while True:
    print("É sua vez de jogar")
    inicio = Baralho()
    cartas = inicio.todas_cartas()
    i = 0
    while len(cartas) >= 1:
        if len(cartas) == 52:
            while True:
                apostar.__init__()
                valor = int(input("Deseja apostar quanto? "))
                if valor > apostar.caixa and type(valor) == int:
                    print("Saldo insuficiente")
                else:
                    break
        if i < 2:
            print(cartas[0])
            inicio.soma_cartas(inicio.pega_carta(cartas))
            i += 1
        else:
            if inicio.pontuacao > 21:
                print("Sua pontuação é de: ", inicio.pontuacao)
                print("Voce perdeu, estourou a pontuação")
                apostar.menos(valor)
                break
            else:
                print("Sua pontuação é de: ", inicio.pontuacao)
                maisCarta = input("Mais uma carta? S/N ").upper()
                if maisCarta == "S":
                    i = 1
                else:
                    print()
                    print("Sua pontuação é de: ", inicio.pontuacao)
                    break
    if inicio.pontuacao < 21:
        inicio.guarda_resultado(inicio.pontuacao)
        inicio.pontuacao = 0
        play = CPU(cartas)
        play.jogada(apostar)

    if input("Deseja parar?").upper() == 'S':
        break
