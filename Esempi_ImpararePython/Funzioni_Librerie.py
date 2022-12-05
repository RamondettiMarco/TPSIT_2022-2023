import random #importo tutta la libreria
from math import sqrt #importo solo la funzione sqrt
#from math import * #vuol dire che uso le funzioni direttamente

for i in range(10):
    val = random.randint(1, 50)
    print(val)
    
print('radice quadrata:')
print(sqrt(25))