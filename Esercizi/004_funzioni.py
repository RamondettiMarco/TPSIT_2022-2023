#funzioni

def print_tre_volte():
    print('ciao')
    print('ciao una seconda volta')
    print('ciao una terza volta')

def sommatrice(a, b):
    print('Questa è la funzione somma')
    print('Fornisce la somma di due numeri passati come parametri')
    r = a + b
    print('Il risultato della somma è ' + str(r))
    #return(r) #meglio perchè le print non si dovrebbero fare nelle funzioni

def laptop_nuovo(ram, cpu, antivirus = False):  #parametro opzionale, posso anche richiamare la funzione con solo due parametri e questo lo mette false
    print('Il nuovo laptop avrà: ')
    print('Ram: ' + ram)
    print('CPU:' + cpu)
    if antivirus == True:
        print('Hai comprato anche l\'antivirus')
    
    
print_tre_volte()

a = int(input('numero 1: '))
b = int(input('numero 2: '))
sommatrice(a, b)

laptop_nuovo('16Gb', 'i7')

laptop_nuovo('8Gb', '15', True)