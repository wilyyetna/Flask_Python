from flask import Flask
from flask import render_template
from flask import json                                                                                                                                     
app = Flask(__name__)                                                                                                                  
#comment

@app.route('/<int:valeur>')
def exercice(valeur):
    etoiles = ''
    for i in range(valeur):
        etoiles += '*'
    return etoiles
#comment

if __name__ == "__main__":
  app.run(debug=True)
Copier/Coller ce code dans votre fichier __init__.py (remplacer votre code d'origine)
```PYTHON
from flask import Flask
from flask import render_template
from flask import json                                                                                                                                     
app = Flask(__name__)                                                                                                                  


@app.route('/<int:valeur>')
def exercice(valeur):
    etoiles = ''
    for i in range(valeur):
        etoiles += '*'
    return etoiles #comm


if __name__ == "__main__":
  app.run(debug=True)
```
