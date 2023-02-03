def inizioFine(function):
    def wrapper():
        print("Inizio Wrapper")
        function()
        print("Fine")
    return wrapper

@inizioFine
def ciao():
    print("Ciao")
    
#ciao = inizioFine(ciao) = a @inizioFine prima della funzione

@inizioFine    
def hello():
    print("Hello")
    
#hello = inizioFine(hello) = a @inizioFine prima della funzione
    
if __name__ == "__main__":
    ciao()
    hello()