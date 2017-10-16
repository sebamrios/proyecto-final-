from servo import *
import virtualenv
from flask import flask

app=Flask(__name__)

servos={}# se crea dicionarios de los servos

@app.route('/servos')# se comprueba por mensaje si esta funcionando
def ControlServo():
    return 'Controlando servos'

@app.route('/NuevoServo/<int::Nid>')#se crea la instancia de servo con id y angulo
def NuevoServo(Nid):
    servos[Nid]=Servo(Nid)
    return ('Servo ID %s  creado', %Nid)

@app.route('/Servo/Mover/<int::Angulo>')#se mueve el servo numero id en un angulo
def mover(Angulo):
    try:
        mensaje=servo[Nid].mover(Angulo)
        print mensaje
    except KeyError:
        return ("Ha ocurrido un error, no exite servo con el ID: %s" %Nid)
    except:
        return ("Ha ocurrido un error inesperado, intente otra vez")

If __name__=="__main__":
    app.run(host="0.0.0.0", port=int("5000"))
