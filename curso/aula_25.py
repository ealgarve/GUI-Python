# herança em classes
class NPC: # base, pai ou super
    def __init__(self, nome, time, forca, municao): # construtor
        self.nome = nome
        self.time = time
        self.forca = forca
        self.municao = municao
        self.vivo = True
        self.energia = 100

    def info(self):
        print(f'Nome....: {self.nome}')
        print(f'Time....: {self.time}')
        print(f'Força...: {self.forca}')
        print(f'Munição.: {self.municao}')
        print(f'Vivo....: {"sim" if self.vivo else "nao"}')
        print(f'Energia.: {self.energia}')
        print('-'*30)

class soldado(NPC): # classe filho de  NPC
    def __init__(self, nome, time): # parametros da clase filho que seão repassadps a classe pai
        self.forca = 200  # parametros internos que tambem serão repassados ao pai
        self.municao = 200
        super().__init__(nome, time, self.forca, self.municao) # repassa parametros ao contrutor da classe pai

class guarda(NPC):
    def __init__(self, nome, time):
        self.forca = 100
        self.municao = 20
        super().__init__(nome, time, self.forca, self.municao)

class elite(NPC):
    def __init__(self, nome, time):
        self.forca = 400
        self.municao = 500
        super().__init__(nome, time, self.forca, self.municao)
    def inf(self):
        super().info()

s1 = guarda('Olho Vivo', 1)
s2 = soldado('Bala na Agulha', 1)
s3 = elite('Ninja', 1)
s4 = guarda('Super Atento', 2)
s5 = soldado('Tiro Certo', 2)
s6 = elite('Samurai', 2)

s1.vivo = False
s3.vivo = False
s3.forca = 10000

s1.info()
s2.info()
s3.info()
s4.info()
s5.info()
s6.inf()