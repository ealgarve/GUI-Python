# https://www.youtube.com/watch?v=t7wjLDQNVJg&list=PLx4x_zx8csUhuVgWfy7keQQAy7t1J35TR&index=22
'''
- Funções curtas
- nome da variavel = lambda arg: expressão
'''

soma = lambda a, b: a + b
print(soma(2, 5))

print((lambda c, d: c * d)(2, 4))
print('-'*10)
for x in range(5):
    a = lambda x, func:func(x)
    print(f'f({x}) = {a(x, lambda x: x * 2)}')
print('-'*10)
for x in range(5):
    y = lambda x: x * x
    print(f'f({x}) = {y(x)}')