def ler_valor2():
    lista = []
    while True:
        valor = input('Digite um número: ')
        try:
            lista.append(int(valor))
        except:
            break
    return lista

def eh_par(x):
    return x % 2 == 0

def ler_valor():
    while True:
        valor = input('Digite um número: ')
        try:
            yield int(valor)
        except:
            # raise StopIteration()
            return


gen = ler_valor()
while True:
    try:
        valor = next(gen)
        if eh_par(valor):
            print(f'{valor} é par')
        else:
            print(f'{valor} é ímpar')    
    except StopIteration:
        pass


for valor in ler_valor():
    if eh_par(valor):
        print(f'{valor} é par')
    else:
        print(f'{valor} é ímpar')

# while True:
#     valor = input('Digite um número:')
#     try:
#         valor = int(valor)
#     except ValueError:
#         print(f'Just "do" it')
#         break

#     if eh_par(valor):
#         print('%d é par' % valor)
#         print('{} é par'.format(valor))
#         print('{1} é par {0}'.format(valor, 'oi'))
#         print('{n:3d} é par'.format(n=valor))
#         print(f'{valor:3d} é par')
#     else:
#         print(f'{valor} é ímpar')
