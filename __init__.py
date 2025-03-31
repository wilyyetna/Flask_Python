from flask import Flask

app = Flask(__name__)

@app.route('/<int:valeur>')
def exercice(valeur):
    etoiles = ''
    for i in range( valeur ,0, -1):
        etoiles += '*' * i + '<br>'
    return etoiles

if __name__ == "__main__":
    app.run(debug=True)
