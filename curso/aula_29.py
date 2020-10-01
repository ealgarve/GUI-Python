Carros = ['HRV', 'Polo', 'Jetta', 'Palio', 'Fusca']
itCarros = iter(Carros)

while itCarros:
    try:
        print(next(itCarros))
    except StopIteration:
        print('Fim da Lista.')
        break