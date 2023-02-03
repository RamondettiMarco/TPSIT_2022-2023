from flask import Flask, jsonify, request
import sqlite3 as sql

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
@app.route("/api/v1/percorsi/<id>", methods=['GET'])
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

def main():   
    app.run()
   


# http://127.0.0.1:5000/api/v1/percorsi/0
if __name__ == "__main__":
    main()