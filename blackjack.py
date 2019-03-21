import random


class Baralho(object):
    """
        Cria um baralho e distribui as cartas
    """
    def __init__(self):
        self.naipe = ('copas', 'espadas', 'ouro', 'paus')
        self.valor = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13')
        self.pontuacao = 0

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
        self.pontuacao += int(valor_dado)
        print(tupla[1])


class Aposta(object):
    caixa = 10000

    def __init__(self):
        if self.caixa <= 0:
            print("Fim de jogo")
        else:
            print("Seu caixa é de: ", self.caixa)

    def deposito(self, valor1):
        self.caixa += valor1

    def debito(self, valor2):
        self.caixa -= valor2


inicio = Baralho()
cartas = inicio.todas_cartas()
print(len(cartas))
print(cartas)
i = 0
while len(cartas) >= 1:
    if len(cartas) == 52:
        apostar = Aposta()
        while True:
            valor = int(input("Deseja apostar quanto? "))
            if valor > apostar.caixa:
                print("Saldo insuficiente")
            else:
                break
    if i < 2:
        print(cartas[0])
        inicio.soma_cartas(inicio.pega_carta(cartas))
        i += 1
    else:
        print(inicio.pontuacao)
        maisCarta = input("Mais uma carta? S/N").upper()
        if maisCarta == "S":
            i = 1
        else:
            print(inicio.pontuacao)
            break
