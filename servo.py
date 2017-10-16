class Servo():
    """docstring for ."""
    def __init__(self,id,angulo=0):
        self.id=id
        self.angulo=angulo

    def mover(id,angulo):
        #radio.send(id,angulo)
        print("servo id %s con angulo %s", id, angulo)
        return(self.id, self.angulo)

    def info(id):
        #radio.send(id)
        print("servo id %s con angulo", id)
