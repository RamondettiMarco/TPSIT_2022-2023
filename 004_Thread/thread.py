import threading
#from threading import Thread
import time

luc = threading.Lock()

def funzione_num(num):
    print(f"Partenza del thread {num}")
    print(f"Elaboro...thread {num}")
    time.sleep(2)
    print(f"Finito lavoro del thread {num}")
    
def funzione():
    print(f"Partenza del thread {threading.current_thread().name}")
    print(f"Elaboro...thread {threading.current_thread().name}")
    time.sleep(2)
    print(f"Finito lavoro del thread {threading.current_thread().name}")

#il main di default è già un thread "MainThread"  
def main():
    t = threading.Thread(target=funzione, name="Primo") #target=funzione_num, args=(1,)
    t.start() #fa partire il thread
    t.join() #fa finire il thread "t" prima di iniziare i successivi, vanno sequenzialmente
    q = threading.Thread(target=funzione, name="Secondo") #target=funzione_num, args=(2,)
    q.start()
    q.join()
    #funzione_num(3) 
    funzione()
    print("Fine chiamata main.")
    
if __name__ == "__main__":
    main()
    