while True:
    try:
        num = int(input('Digite um valor positivo: '))
        if num < 0:
            raise ValueError('Valor Negativo') # print(f'--> {num} é um valor negativo, logo não é permitido.')
        elif num >= 0:
                print(f'--> {num} é um valor positivo.')
                
        else:
            print('Ops, algo deu errado')
    except ValueError:
        print('ERRO: entrada invaliada, o valor deve ser positivo')
        #continue
    else:
        print('Você digitou corretamente.')
        break
    finally:
        print('Volte sempre!!!')
        pass

