import turtle as t 
from math import cos, sin
# Escribir el texto "Te amo Eliana" en el centro
t.tracer(2,0.5)
t.bgcolor('black')
t.color('red')

def heartx(n:int):
    x = 15*sin(n)**3
    return x
def hearty(n:int):
    y = 12*cos(n)-5*cos(2*n)-2*cos(3*n)-cos(4*n)
    return y


for i in range(800):
    t.goto(heartx(i)*10,hearty(i)*10)
    t.goto(0, 0)  # Mover al centro del corazón

t.color('white')  # Color del texto
t.write("Te amo Eliana", align="center", font=("Arial", 24, "bold"))
t.exitonclick()