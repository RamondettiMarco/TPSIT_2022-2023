#leggere e scrivere file in json
import json
from flask import Flask, jsonify

app = Flask(__name__)
@app.route("/api/v1/percorsi")
def percorsi():
    pass

#passo come parametro della funzione
@app.route("/api/v1/percorsi/<id>")
def percorso(id):
    percorso = {"id": id}   #qua ci sarà una query al db
    #return json.dumps(percorso)    #NON imposta il content-type quindi non va bene perchè chi 
                                    #riceve non sa che tipo di dato ha ricevuto
    return jsonify(percorso)     #imposta anche il content-type

def main():
    """movimento = {"id" : 0, "nome":"avanti"}
    print(movimento)
    print(json.dumps(movimento))

    stringa_movimento = '{"id" : 0, "nome" : "avanti"}'
    decodifica = json.loads(stringa_movimento)
    print(decodifica)"""

    app.run()


# http://127.0.0.1:5000/api/v1/percorsi/0
if __name__ == "__main__":
    main()

