"""
EVALUACIÓN UNIDAD III
RAMO: PROGRAMACIÓN WEB
ALUMNO: FRANCISCO MÉNDEZ Y.
"""
from flask import Flask, render_template, request
app = Flask(__name__)

# Definición de página de inicio
@app.route('/')
def index():
    return render_template('index.html')

# Desarrollo Ejercicio 1
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    msg = None
    estado = None
    promedio = 0
    mostrarResultado = False
    if request.method == 'POST':
        try:
            # Notas las guarde en listas
            notas = [
                float(request.form['nota1']),
                float(request.form['nota2']),
                float(request.form['nota3'])
            ]
            asistencia = float(request.form['asistencia'])
            for nota in notas:
                if nota < 10 or nota > 70:
                    break
            else:
                promedio = round(sum(notas) / len(notas),2)# Calculo el promedio con el array
                if promedio >= 40 and asistencia >= 75:
                    estado = "APROBADO"
                else:
                    estado = "REPROBADO"
            mostrarResultado = True
        except ValueError:
            msg = "Sólo puedes ingresar valores numericos para las notas y la asistencia."
    return render_template('ejercicio1.html', estado=estado, promedio=promedio, mostrarResultado=mostrarResultado )

# Desarrollo Ejercicio 2
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    nombreLargo = None
    longitudLargo = None
    if request.method == 'POST':
        nombres = [
            request.form['nombre1'],
            request.form['nombre2'],
            request.form['nombre3']
        ]
        nombreLargo = max(nombres, key=len)
        longitudLargo = len(nombreLargo)
    return render_template('ejercicio2.html', nombre=nombreLargo, longitud=longitudLargo)

if __name__ == '__main__':
    app.run(debug=True)