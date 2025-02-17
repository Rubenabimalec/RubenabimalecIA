import turtle as t
steps=100
#angle=90
#Matrizes que contienen las coredenadas del cubo, el segundo es proporcionalmente siempre con respecto a la primera matriz.
matriz1=[[0,0],[0, -steps],[-steps, -steps],[-steps, 0]]
matriz2=[[0.5*(steps), 0.5*(-steps)],[0.5*(steps), 1.5*(-steps)],[0.5*(-steps), 1.5*(-steps)],[0.5*(-steps), 0.5*(-steps)]]
#matriz1=[[0,0],[0,-100],[-100,-100],[-100,0]]
#matriz2=[[50,50],[50,-50],[-50,-50],[-50,50]]

def buildCubo(matriz1,matriz2):
    t.speed(1)

    #dibujando el primer cuadro
    t.penup()
    t.goto(matriz1[0])#se mueve al primer punto de la matriz
    t.pendown()
    for i in range(4):
        t.goto(matriz1[i])
    t.goto(matriz1[0])
   


    #dibujando el segundo cuadroi
    t.penup()
    t.goto(matriz2[0])#se mueve al primer punto de la matrizi  
    t.pendown()
    for i in range(4):
        t.goto(matriz2[i])    
    t.goto(matriz2[0])
    t.penup()

    #uniendo los vertices, union de los vertices de cada cuadrado[x,y][x,y]
    for i in range (4):
        t.goto(matriz1[i])
        t.pendown()
        t.goto(matriz2[i])
        t.penup()
    t.done()

buildCubo(matriz1,matriz2)
