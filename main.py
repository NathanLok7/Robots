#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# Declaracion de objetos 

ev3 = EV3Brick()
motor1 = Motor(Port.A,positive_direction=Direction.COUNTERCLOCKWISE,gears=[40,20])
motor2 = Motor(Port.B,positive_direction=Direction.COUNTERCLOCKWISE,gears=[40,20])
motor3 = Motor(Port.C,positive_direction=Direction.CLOCKWISE,gears=[40,20])
motor4 = Motor(Port.D,positive_direction=Direction.CLOCKWISE,gears=[40,20])
Sensor_luz = ColorSensor(Port.S1)
ultrasonico = InfraredSensor(Port.S2)

contador_giros = 0

#Funcion para mover los motores simultaneamente

def mover_motores_adelante(velocidad):
    motor1.run(velocidad)
    motor2.run(velocidad)
    motor3.run(velocidad)
    motor4.run(velocidad)

#Funcion para parar los motores simultaneamente

def parar_motores():
    motor1.stop()
    motor2.stop()
    motor3.stop()
    motor4.stop()

#Funcion para girar a la izquierda
def izquierda():
    global contador_giros
    if contador_giros < 2:
        motor1.run(-1500)
        motor2.run(700)
        motor3.run(-1500)
        motor4.run(700)
        wait(1000)
        contador_giros += 1
    else:
        # En el tercer giro, gira más
        motor1.run(-1500)
        motor2.run(700)
        motor3.run(-1500)
        motor4.run(700)
        wait(2000)
        contador_giros = 0  # Reinicia el contador después del tercer giro


def primer_izquierda():
    motor1.run(1500)
    motor2.run(-700)
    motor3.run(1200)
    motor4.run(-700)
    wait(1700)

#Estructura logica 

def logica():

    #Girar en caso de detectar blaco y no detectar nada enfrente 

    if Sensor_luz.color() == Color.WHITE:
        parar_motores()
        while Sensor_luz.color() == Color.WHITE:
            izquierda()
            
    #Avanzar mientras se detecte un color que no sea blanco o se detecte un objeto enfrente 

    else:
        mover_motores_adelante(10000)

primer_izquierda()
while True:
    if ultrasonico.distance() != 100 and Sensor_luz.color() != Color.WHITE:
            mover_motores_adelante(10000)
    else:
        logica()