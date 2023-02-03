from flask import Flask, jsonify, request
import sqlite3 as sql
import time
from Alphabot1 import AlphaBot
import RPi.GPIO as GPIO

Ab = AlphaBot()

def controllo_comandi(comando,tempo):
    global Ab
    if comando.upper() == "AVANTI": #avanti
        Ab.forward()
        time.sleep(float(tempo))        #durata del movimento
        Ab.stop()
    if comando.upper() == "GIRADX": #destra
        Ab.right()
        time.sleep(float(tempo))   
        Ab.stop()
    if comando.upper() == "INDIETRO": #indietro
        Ab.backward()
        time.sleep(float(tempo))   
        Ab.stop()
    if comando.upper() == "GIRASX": #sinistra
        Ab.left()
        time.sleep(float(tempo))   
        Ab.stop()
    if comando.upper() == "ESCI": #fermo
        Ab.stop()

app = Flask(__name__)

@app.route("/api/v1/percorsi", methods=['POST'])
def creaPercorso():
    dati = request.get_json()
    #print(dati["nome"])
    try:
        with sql.connect("./percorsi.db") as connection:
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO Percorso (nome) VALUES(?)''',(dati["nome"],))
            connection.commit()
    except Exception as e:
        temp = {"success": False, "error": str(e)}
        
    return jsonify(temp)

@app.route("/api/v1/percorsi", methods=['GET'])
def leggiPercorsi():
    try:
        with sql.connect("./percorsi.db") as connection:
            cursor = connection.cursor()
            cursor.execute('''SELECT * FROM Percorso''')
            percorsi = cursor.fetchall()
            temp = [{"success": True, "id":percorso[0], "name":percorso[1]} for percorso in percorsi]
            connection.commit()
    except Exception as e:
        temp = {"success": False, "error": str(e)}

        
    return jsonify(temp)

#passo come parametro della funzione
@app.route("/api/v1/percorsi/<id>")
def leggiPercorso(id):
    try:
        with sql.connect("./percorsi.db") as connection:
            cursor = connection.cursor()
            cursor.execute('''SELECT Percorso.id, Percorso.nome, Mossa.posizione, Movimento.nome, Mossa.tempo FROM Percorso, Movimento, Mossa WHERE Percorso.id = ? AND Mossa.codPercorso = Percorso.id AND Movimento.id = Mossa.codMovimento ORDER BY Mossa.posizione''', (id,))  #qua ci sarà una query al db
            percorso = cursor.fetchall()
            temp = [{"success": True, "idPercorso":info[0], "namePercorso":info[1], "posizioneMossa":info[2], "movimento":info[3], "tempo":info[4]} for info in percorso]
            connection.commit()
    except Exception as e:
        temp = {"success": False, "error": str(e)}
    return jsonify(temp)    #imposta anche il content-type

@app.route("/api/v1/percorsi/<id>/muovi", methods=['GET'])
def muovi(id):
    try:
        with sql.connect("./percorsi.db") as connection:
            cursor = connection.cursor()
            cursor.execute('''SELECT Percorso.id, Percorso.nome, Mossa.posizione, Movimento.nome, Mossa.tempo FROM Percorso, Movimento, Mossa WHERE Percorso.id = ? AND Mossa.codPercorso = Percorso.id AND Movimento.id = Mossa.codMovimento ORDER BY Mossa.posizione''', (id,))  #qua ci sarà una query al db
            percorso = cursor.fetchall()
            temp = [{"success": True, "idPercorso":info[0], "namePercorso":info[1], "posizioneMossa":info[2], "movimento":info[3], "tempo":info[4]} for info in percorso]
            connection.commit()
            
            for i in range(0, len(temp)):
                comando, tempo = temp[i]["movimento"], temp[i]["tempo"]
                controllo_comandi(comando, tempo)
            
    except Exception as e:
        temp = {"success": False, "error": str(e)}
    return jsonify(temp)    #imposta anche il content-type

def main():   
    app.run(host="0.0.0.0")
   


# http://127.0.0.1:5000/api/v1/percorsi/0
# AB25: 192.168.1.122
if __name__ == "__main__":
    main()