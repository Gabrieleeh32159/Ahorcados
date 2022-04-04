from turtle import*
#Base
penup()
goto(-100, -200)
pendown()
for x in range(-100, 101, 1):
    goto(x, -220)
    goto(x, -200)
goto(0, -200)
#Primer error
goto(0,200)
#Segundo error
goto(200,200)
#Tercer error
goto(200,180)
#Cuarto error
circle(-20)
penup()
goto(200, 140)
pendown()
#Quinto error
goto(200, 0)
#Sexto error
goto(150, -30)
penup()
goto(200,0)
pendown()
#Séptimo error
goto(250, -30)
penup()
goto(200, 100)
pendown()
#Octavo error
goto(150,70)
penup()
goto(200, 100)
pendown()
#Noveno error
goto(250, 70)
input()
