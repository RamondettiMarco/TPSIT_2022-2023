class Persona:
    
    istituto = "Scuola Superiore"
    
    def __init__(self, nome, cognome, eta, residenza):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
        self.residenza = residenza
     
    @classmethod #per passare come parametro una classe
    def fromString(cls, stringa_persona, *args): #self lavora su valori, io voglio passare una classe con cls
        nome, cognome, eta, residenza = stringa_persona.split('-')
        return cls(nome, cognome, eta, residenza, *args)
    
    @classmethod
    def occupazione(cls):
        if cls.__name__=="Studente":
           return "Studente"
        else:
            return "Insegnante" 
        
    @staticmethod
    def info():
        info = """
        Nome: Persona
        Creato da: Ramo
        Commenti: Scritto usando Python 3.10"""
        
        return info
        
    def schedaPersonale(self):
        scheda = f"""
        Nome: {self.nome}
        Cognome: {self.cognome}
        Età: {self.eta}
        Residenza: {self.residenza}\n"""
        
        return scheda
    
    def modificaSchedaPersonale(self):
        print("""Modifica Scheda:
        1 - Nome
        2 - Cognome
        3 - Età
        4 - Residenza""")
        
        scelta = input("Cosa desideri modificare? ")
        if scelta == "1":
            self.nome = input("Nuovo Nome --> ")
        if scelta == "2":
            self.cognome = input("Nuovo Cognome --> ")
        if scelta == "3":
            self.eta = input("Nuova Eta --> ")
        if scelta == "4":
            self.residenza = input("Nuova Residenza --> ")

class Studente(Persona):
    profilo = "Studente"
    
    def __init__(self, nome, cognome, eta, residenza, corso):
        super().__init__(nome, cognome, eta, residenza)
        self.corso = corso
        
    def schedaPersonale(self):
        scheda = f"""
        Profilo: {Studente.profilo}
        Corso di Studi: {self.corso}\n"""
        
        return super().schedaPersonale() + scheda
    
    def cambioCorso(self, corsoNuovo):
        self.corso = corsoNuovo
        print("Corso Aggiornato")
        

class Insegnante(Persona):
    profilo = "Insegnante"
    
    def __init__(self, nome, cognome, eta, residenza, materie = None):
        super().__init__(nome, cognome, eta, residenza)
        if materie is None:
            self.materie = []
        else:
            self.materie = materie
            
    def schedaPersonale(self):
        scheda = f"""
        Profilo: {Insegnante.profilo}
        Materie insegnate: {self.materie}\n"""
        
        return super().schedaPersonale() + scheda
    
    def aggiungiMateria(self, nuova):
        if nuova not in self.materie:
            self.materie.append(nuova)
        print("Elenco Materie Aggiornato")

studente1 = Studente("Marco", "Ramondetti", 17, "CP", "informatica")
insegnante1 = Insegnante("Tom", "Levro", 17, "Beine", ["italiano", "storia"])
print(studente1.schedaPersonale())
print(insegnante1.schedaPersonale())
insegnante1.modificaSchedaPersonale()
insegnante1.aggiungiMateria("Filosofia")
studente1.cambioCorso("Fisica")
print(studente1.schedaPersonale())
print(insegnante1.schedaPersonale())

#print(help(Studente))

ironMan = "Tony-Stark-40-Torre Stark"
zuck = "Mark-Zuckerberg-33-California"
persona1 = Persona.fromString(ironMan)

ins = Insegnante.fromString(ironMan)
print(ins.occupazione())
std = Studente.fromString(zuck, 'corso')
print(std.occupazione())

print(Persona.info())