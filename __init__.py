from flask import Flask

app = Flask(name)

Fonction pour générer la suite de Fibonacci jusqu'à n
def fibonacci(n):
    fib = [0, 1] 
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])  
    return fib

@app.route('/<int:n>')
def afficher_fibonacci(n):

    if n == 1:
        fib_sequence = [0]
    else:
    
        fib_sequence = fibonacci(n)

Convertir la suite en chaîne pour l'affichage
    result = ', '.join(map(str, fib_sequence))

Retourner le résultat formaté
    return f"<h1>Suite de Fibonacci jusqu'au {n}-ième terme :</h1><p>{result}</p>"

if name == "main":
    app.run(debug=True)

