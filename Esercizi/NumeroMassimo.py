"""esercizio 002: max tra tre numeri"""
print('\nES_002')
def maxTraTreNumeri(n1, n2, n3):
    if n1 >= n2 and n1 >= n3:
        print('il numero maggiore è: ' + str(n1))
    elif n2 >= n3 and n2 >= n3:
        print('il numero maggiore è: ' + str(n2))
    else:
        print('il numero maggiore è: ' + str(n3))

    if n1 == n2 and n1 == n3:
        print('e i tre numeri sono uguali')


n1 = int(input('Inserire il numero 1: '))
n2 = int(input('Inserire il numero 2: '))
n3 = int(input('Inserire il numero 3: '))
maxTraTreNumeri(n1, n2, n3)