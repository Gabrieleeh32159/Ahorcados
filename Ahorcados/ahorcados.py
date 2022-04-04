from turtle import*
from random import choice
import os
palabras = ["humanidad", "humano", "persona", "gente", "hombre", "mujer", "niño", "niña", "adolescente", "adulto", "adulta", "anciano", "anciana", "don",
"doña", "señor", "caballero", "dama", "individuo", "cuerpo", "pierna", "pie", "rodilla", "muslo", "cabeza", "cara", "boca", "labio", "diente", "ojo",
"nariz", "barba", "bigote", "cabello", "oreja", "cerebro", "estómago", "brazo", "codo", "hombro", "uña", "mano", "muñeca", "palma", "dedo", "músculo",
"cuello", "mente", "alma", "pecho", "cintura", "cadera", "espalda", "sangre", "carne", "piel", "hueso", "resfriado", "gripe", "salud", "enfermedad",
"familia", "amigo", "conocido", "colega", "pareja", "esposo", "matrimonio", "amor", "padre", "madre", "hermano", "hijo", "abuelo", "bisabuelo", "nieto",
"bisnieto", "primo", "sobrino", "criatura", "especie", "ser", "vida", "nacimiento", "muerte", "naturaleza", "campo", "bosque", "selva", "jungla",
"desierto", "costa", "playa", "laguna", "lago", "mar", "cerro", "monte", "montaña", "luz", "animal", "perro", "gato", "vaca", "cerdo", "caballo", "yegua"
"oveja", "mono", "rata", "tigre", "conejo", "ciervo", "rana", "jirafa", "elefante", "gallina", "cuervo", "águila", "pez", "langosta", "sardina", "atún",
"calamar", "pulpo", "insecto", "bicho", "mariposa", "polilla", "saltamontes", "araña", "mosca", "mosquito", "cucaracha", "caracol", "babosa", "lombriz",
"marisco", "molusco", "lagarto", "serpiente", "cocodrilo", "alimento", "comida", "bebida", "vegetal", "planta", "pasto", "flor", "fruta", "semilla",
"hoja", "tallo", "hongo", "ciruela", "pino", "nuez", "almendra", "castaña", "arroz", "avena", "cebada", "trigo", "verdura", "patatas", "papas",
"guisantes", "zanahoria", "manzana", "naranja", "pera", "castaño", "durazno", "tomate", "carne", "gaseosa"]

print("Cargando...")
penup()
goto(-100, -200)
pendown()
for x in range(-100, 101, 1):
    goto(x, -220)
    goto(x, -200)
goto(0, -200)

palabra_elegida = choice(palabras)
adivinar = False
palabra_con_intentos = []
for i in range(len(palabra_elegida)):
    palabra_con_intentos.append("_")
fallos = 0
print("Bienvenido a Ahorcados!, este juego trata de adivinar una palabra aleatoria.")
print("La palabra consta de {} letras".format(len(palabra_elegida   )))
while adivinar == False:
    print(" ".join(palabra_con_intentos))
    char_intento = input("Qué letra cree que está en la palabra? :")
    cantidad_apariciones_letra = 0
    for i in range(len(palabra_elegida)):
        if char_intento == palabra_elegida[i]:
            palabra_con_intentos.pop(i)
            palabra_con_intentos.insert(i, char_intento)
            cantidad_apariciones_letra += 1
    if cantidad_apariciones_letra > 0:
        print("Correcto!! Esa letra estaba en la palabra!!")
    else:
        fallos += 1
        print("No... sigue intentando")
        if fallos == 1:
            goto(0,200)
        elif fallos == 2:
            goto(200,200)
        elif fallos == 3:
            goto(200,180)
        elif fallos == 4:
            circle(-20)
            penup()
            goto(200, 140)
            pendown()
        elif fallos == 5:
            goto(200, 0)
        elif fallos == 6:
            goto(150, -30)
            penup()
            goto(200,0)
            pendown()
        elif fallos == 7:
            goto(250, -30)
            penup()
            goto(200, 100)
            pendown()
        elif fallos == 8:
            goto(150,70)
            penup()
            goto(200, 100)
            pendown()
        elif fallos == 9:
            goto(250, 70)
    if "".join(palabra_con_intentos) == palabra_elegida :
        print("Felicidades!! Ganaste!! La palabra era: {}".format(palabra_elegida))
        print("Lo lograste teniendo {} fallos".format(fallos))
        adivinar = True
    elif fallos == 9:
        print("Lo siento, llegaste a 9 fallos y la personita se ahorcó :(")
        print("La palabra correcta era {}".format(palabra_elegida))
        adivinar = True
        input()
