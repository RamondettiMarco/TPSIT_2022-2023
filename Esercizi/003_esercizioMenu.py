while True:
    print('''
    Benvenuto al programma calcolatrice!
    Di seguito un elenco delle varie funzioni disponibili:

    -Per effettuare un'ADDIZIONE, seleziona 1;
    -Per effettuare una SOTTRAZIONE, seleziona 2;
    -Per effettuare una MOLTIPLICAZIONE, selezionare 3;
    -Per effettuare una DIVISIONE, seleziona 4;
    -Per effettuare un calcolo ESPONENZIALE, seleziona 5;
    -Per uscire dal programma puio digitare ESC;
    ''')

    scelta = input('Inserisci il numero corrispondente all\'operazione selezionata: ')
    if scelta == '1':
        print('\nHai scelto ADDIZIONE')
        a = float(input('numero 1: '))
        b = float(input('numero 2: '))
        print('Il risultato della somma è: ' + str(a+b))
    elif scelta == '2':
        print('\nHai scelto SOTTRAZIONE')
        a = float(input('numero 1: '))
        b = float(input('numero 2: '))
        print('Il risultato della sottrazione è: ' + str(a-b))
    elif scelta == '3':
        print('\nHai scelto MOLTIPLICAZIONE')
        a = float(input('numero 1: '))
        b = float(input('numero 2: '))
        print('Il risultato della moltiplicazione è: ' + str(a*b))
    elif scelta == '4':
        print('\nHai scelto DIVISIONE')
        a = float(input('numero 1: '))
        b = float(input('numero 2: '))
        print('Il risultato della divisione è: ' + str(a/b))
    elif scelta == '5':
        print('\nHai scelto ESPONENZIALE')
        a = float(input('base: '))
        b = float(input('esponente: '))
        print('Il risultato della sottrazione è: ' + str(a**b))
    elif scelta == 'ESC':
        #sforzo l'uscita
         break;   
    else:
        print("\nopzione non disponibile.")
    
    #per finire il ciclo uso il break 
    loop = input('Vuoi terminare il programma? (S/N)')
    if loop == 's' or loop == 'S':
        #sforzo l'uscita
        break
    else:
        #continuo il programma
        continue

