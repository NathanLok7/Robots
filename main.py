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
    motor1.run(-3000)
    motor2.run(1800)
    motor3.run(-3000)
    motor4.run(1800)
    wait(1000)


def primer_izquierda():
    motor1.run(-4000)
    motor2.run(2800)
    motor3.run(-4000)
    motor4.run(2800)
    wait(1600)

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

##hola