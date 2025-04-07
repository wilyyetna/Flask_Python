from flask import Flask

app = Flask(name)

@app.route('/<path:valeurs>')
def exercice(valeurs):
    liste_nombres = valeurs.split('/')
    liste_nombres = [int(n) for n in liste_nombres]

    # Trouver le maximum et son indice sans utiliser max()
    max_val = liste_nombres[0]
    max_index = 0

    for i in range(1, len(liste_nombres)):
        if liste_nombres[i] > max_val:
            max_val = liste_nombres[i]
            max_index = i

    return f"Le plus grand nombre est : {max_val}, à l'indice : {max_index}"

if name == 'main':
    app.run(host='0.0.0.0')
