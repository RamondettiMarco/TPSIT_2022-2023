
class Studente:

    ore = 36
    corpo_studentesco = 0

    def __init__(self, nome, cognome, corso): #self rappresenta l'istanza passata automaticamente, guarda print(Studente.schedaPersonale(studente1))
        self.nome = nome
        self.cognome = cognome
        self.corso = corso

    def schedaPersonale(self):
        return f"Scheda Studente:\n Nome: {self.nome}\n Cognome: {self.cognome}\n Corso: {self.corso}\n Ore Settimanali: {self.ore}\n"

studente1 = Studente("Marco", "Ramondetti", "Programmazione")
studente2 = Studente("Tommaso", "Levrone", "Lettere")    

studente1.ore += 4

print(studente1.schedaPersonale())
print(studente2.schedaPersonale())

print(Studente.schedaPersonale(studente1)) #uguale a print(studente1.schedaPersonale()), ma passo un'istanza al posto di self richiamando il metodo direttamente con la classe

print(Studente.__dict__)
print(studente1.__dict__)