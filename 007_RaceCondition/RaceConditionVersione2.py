from threading import Thread
import time

class Increasing(Thread):
    def __init__(self, x):
        Thread.__init__(self)
        self.x = x
        
    def increment(self):
        for _ in range(10000):
            self.x = self.x + 1

class ThreadIncrement(Thread):
    def __init__(self, x):
        Thread.__init__(self)
        self.x = x
    def run(self):
        Increasing(self.x.increment())

#il main di default è già un thread "MainThread"  
def main():
    lista_threads = []
    x = Increasing(0)
    
    for i in range(1000):
        lista_threads.append(ThreadIncrement(x))
    
    for k in range(len(lista_threads)):
        lista_threads[k].start()
        
    for j in range(len(lista_threads)):
        lista_threads[j].join()
        
    print("Fine chiamata main.")
    print(f"VALORE FINALE VARIABILE -> {x.x}")
    if x.x != (1000*10000): #il risultato dovrebbe essere (1000*10000)
        print("Si è verificato un fenomeno di Race Condition")
    
if __name__ == "__main__":
    main()