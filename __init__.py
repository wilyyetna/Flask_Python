from flask import Flask
from flask import render_template
from flask import json


app = Flask(name)

@app.route('/<int:valeur>')
def exercice(valeur):
    somme = 0
    for i in range(1, valeur + 1):
        if i % 11 == 0:
            continue
        if i % 5 == 0 or i % 7 == 0:
            if somme + i > 5000:
                break
            somme += i

    return f'<pre>Somme finale: {somme}</pre>'

if name == "main":
    app.run(debug=True)

