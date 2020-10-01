class carro:
    velMax = 0
    ligado = False
    cor = ''
    def __init__(self, v, l, c): # contrutor. self referencia o metodos a classe
        self.velMax = v
        self.ligado = l
        self.cor = c

    def mostrar(self):
        print(f'velocidade Máxima...: {self.velMax}')
        print(f'Cor.................: {self.cor}')
        estado = 'sim' if self.ligado else 'não'
        print(f'Ligado..............: {estado}')
        print("-"*30)

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

    def andar(self):
        if self.ligado:
            print('andando')
        else:
            print('carro desligado')

c1 = carro(100, False, 'branco')
c2 = carro(200, False, 'preto')
c3 = carro(350, False, 'vermelho')


c1.ligar()

c1.mostrar()
c2.mostrar()
c3.mostrar()

c1.andar()
c2.andar()
c3.andar()