from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/somma', methods=['GET']) #è un decorator -> ha come risultato una funzione 
#prende in input "somma" esegue delle operazioni, esegue la funzione "somma" e fa di nuovo altre operazioni
def sommaGet():
    try:
        a = int(request.args.get('txtA'))
        b = int(request.args.get('txtB'))
        c = a+b
        return str(c)
    except:
        return "<h1>ERRORE NELL'INPUT</h1>"
    
@app.route('/somma', methods=['POST']) #è un decorator -> ha come risultato una funzione 
#prende in input "somma" esegue delle operazioni, esegue la funzione "somma" e fa di nuovo altre operazioni
def sommaPost():
    try:
        a = int(request.form.get('txtA'))
        b = int(request.form.get('txtB'))
        c = a+b
        return str(c)
    except:
        return "<h1>ERRORE NELL'INPUT</h1>"

@app.route('/', methods=['GET'])
def homePage():
    return """
    <html>
        <body>
            <form action="/somma" method="POST">
                <label for="primoNumero">
                    Primo Numero -> 
                </label>
                <input type="text" id="primoNumero "name="txtA">
                <br>
                
                <label for="secondoNumero">
                    Secondo Numero -> 
                </label>
                <input type="text" id="secondoNumero "name="txtB">
                <br>
                
                <input type="submit" value="Somma">
            </form>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run()