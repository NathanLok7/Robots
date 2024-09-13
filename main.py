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
blancos = 0
busqueda = True

#Funcion para mover los motores simultaneamente
def mover_motores_adelante():
    motor1.run(10000)
    motor2.run(10000)
    motor3.run(10000)
    motor4.run(10000)

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

#Funcion para girar a la derecha
def derecha():
    motor1.run(3000)
    motor2.run(-1800)
    motor3.run(3000)
    motor4.run(-1800)

#Funcion para girar por primera vez a la izquierda
def primer_izquierda():
    motor1.run(-4000)
    motor2.run(2800)
    motor3.run(-4000)
    motor4.run(2800)
    wait(1500)


primer_izquierda()
while True:
    if ultrasonico.distance() != 100: 
        mover_motores_adelante()
        busqueda = True
        blancos = 0 
        print("Busqueda: {}, Blancos: {}".format(busqueda,blancos))
        while Sensor_luz.color() == Color.BLACK:
            mover_motores_adelante()
    elif Sensor_luz.color() == Color.BLACK and ultrasonico.distance() == 100 and busqueda:
        while Sensor_luz.color() == Color.BLACK:
            mover_motores_adelante()
        busqueda = False
    elif ultrasonico.distance() == 100 and Sensor_luz.color() != Color.BLACK and blancos ==  0:
        parar_motores()
        while Sensor_luz.color() != Color.BLACK:
            izquierda()
        while Sensor_luz.color() == Color.BLACK and ultrasonico.distance() != 100:
            izquierda()
        blancos = 1
    elif ultrasonico.distance() == 100 and Sensor_luz.color() != Color.BLACK and blancos == 1:
        parar_motores()
        while Sensor_luz.color() != Color.BLACK:
            derecha()
        while Sensor_luz.color() == Color.BLACK and ultrasonico.distance() != 100:
            derecha()
        blancos = 0 



