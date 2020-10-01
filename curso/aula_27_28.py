import os
carros = []

class Carro:
    nome = ''
    pot = 0
    velMax = 0
    ligado = False
    def __init__(self, nome, pot):
        self.nome = nome
        self.pot = pot
        self.velMax = int(pot) * 2
        self.ligado = False

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

    def info(self):
        print(f'Nome..........: {self.nome}')
        print(f'Potência......: {self.pot}')
        print(f'Vel. Máxima...: {self.velMax}')
        print(f'Ligado........: {"sim" if self.ligado == True else "não"}')

def menu():
    os.system('cls') or None
    print('1 - Novo Carro')
    print('2 - Informações do carro')
    print('3 - Excluir carro')
    print('4 - Ligar carro')
    print('5 - Desligar carro')
    print('6 - Listar carro')
    print('7 - Sair')
    print(f'Quantidade de carros: {len(carros)}')
    opc = input('Digite uma opção: ')
    return opc

def NovoCarro():
    os.system('cls') or None
    n = input('Nome do carro........: ')
    p = input('Potência do carro....: ')
    car = Carro(n, p)
    carros.append(car)
    print('Novo carro criado.')
    os.system('pause')

def informacoes():
    os.system('cls') or None
    n = input('Informe o numero do carro que deseja ver as informações: ')
    try:
        carros[int(n)].info()
    except:
        print('Carro não existe na lista')
    os.system('pause')

def excluirCarro():
    os.system('cls') or None
    n = input('Informe o numero do carro que deseja excluir: ')
    try:
        del carros[int(n)]
    except:
        print('Carro não existe na lista')
    os.system('pause')

def ligarCarro():
    os.system('cls') or None
    n = input('Informe o numero do carro que deseja ligar: ')
    try:
        carros[int(n)].ligar()
        print('Carro Ligado')
    except:
        print('Carro não existe na lista')
    os.system('pause')

def desligarCarro():
    os.system('cls') or None
    n = input('Informe o numero do carro que deseja desligar: ')
    try:
        carros[int(n)].desligar()
        print('Carro Desligado')
    except:
        print('Carro não existe na lista')
    os.system('pause')

def listarCarro():
    os.system('cls') or None
    for c, p in enumerate(carros):
        print(f'{str(c)} - {p.nome}')
        #p = p + 1
    os.system('pause')

ret = menu()
while ret < '7':
    if ret == '1':
        NovoCarro()
    elif ret == '2':
        informacoes()
    elif ret == '3':
        excluirCarro()
    elif ret == '4':
        ligarCarro()
    elif ret == '5':
        desligarCarro()
    elif ret == '6':
        listarCarro()
    ret = menu()

os.system('cls') or None
print('programa finalizado')