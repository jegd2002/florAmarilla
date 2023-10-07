import math
import turtle
import pygame
import tkinter as tk
from tkinter import messagebox
import time 

pygame.mixer.init()

cancion = pygame.mixer.Sound("florencia.mp3")  

cancion.play()

turtle.bgcolor("black")
turtle.shape("turtle")
turtle.speed(0)
turtle.fillcolor("brown")
turtle.penup()
turtle.goto(0, -200)
turtle.pendown()
turtle.setheading(90)
turtle.fillcolor("green") 
turtle.begin_fill()
turtle.forward(200)
turtle.left(90)
turtle.forward(20)
turtle.left(90)
turtle.forward(200)
turtle.end_fill()
turtle.penup()
turtle.goto(0, -180)
turtle.fillcolor("#8B4513")  
turtle.begin_fill()
turtle.circle(0)
turtle.end_fill()

phi = 137.508 * (math.pi / 180.0)
for i in range(160 + 40):
    r = 4 * math.sqrt(i)
    theta = i * phi
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(i * 137.508)
    turtle.pendown()
    if i < 160:
        turtle.stamp()
    else:
        turtle.fillcolor("yellow")
        turtle.begin_fill()
        turtle.right(20)
        turtle.forward(70)
        turtle.left(40)
        turtle.forward(70)
        turtle.left(140)
        turtle.forward(70)
        turtle.left(40)
        turtle.forward(70)
        turtle.end_fill()


turtle.penup()
turtle.goto(0, 200)  
turtle.color("Red") 
turtle.write("Te Quiero", align="center", font=("Arial", 24, "bold"))


turtle.hideturtle()


time.sleep(5)


root = tk.Tk()
root.withdraw() 
messagebox.showinfo("Mensaje", "Nunca espectadora Siempre protagonista")


turtle.bye()
pygame.mixer.stop()

