import turtle as t
from random import random
angle=90
steps=200
medio=100

##primer cuadrado de frente    
for _ in range(4):
    t.right(angle)
    t.fd(steps)
    t.left(angle)
    angle= angle + 90 
    tp=t.pos()
    print(tp )
##se mueve al centro del primer cuadrado para iniciar el segundo con el primer vertice inicial    
t.goto(-medio,-medio)
##genera el segundo cuadro
for _ in range(4):
    t.right(angle)
    t.fd(steps)
    t.left(angle)
    angle= angle + 90
    tp=t.pos()
    print("posicion:",tp )

##genera cada union de verticesentre el primer cuadro y el segundo 
t.penup()
t.goto(0,2*(-medio))
t.pendown()
t.goto(-medio,3*(-medio))

t.penup()
t.goto(2*(-medio),2*(-medio))
t.pendown()
t.goto(3*(-medio),3*(-medio))

t.penup()
t.goto(2*(-medio),0)
t.pendown()
t.goto(3*(-medio),-medio)


continuar = input('quieres continuar')
