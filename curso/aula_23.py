# aula 23 - Classes (https://www.youtube.com/watch?v=AvS6MNwX3lU&list=PLx4x_zx8csUhuVgWfy7keQQAy7t1J35TR&index=23)

class carro:
    velMax = 0
    ligado = False
    cor = ''

c1 = carro()
c2 = carro()
c3 = carro()

c1.velMax = 200
c1.cor = 'preto'
c1.ligado = False

print(f'velocidade Máxima: {c1.velMax}')
print(f'Cor: {c1.cor}')
estado = 'sim' if c1.ligado else 'não'
print(f'Ligado: {estado}')