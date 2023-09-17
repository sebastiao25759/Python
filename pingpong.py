#simples jogo de pong
# By: Sebastião rodrigues
# Date: 16/09/2023

import turtle

#configuração da tela
wn = turtle.Screen()
wn.title("Pong by Sebastião")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#poddle A
pad_a = turtle.Turtle()
pad_a.speed(0)
pad_a.shape("square")
pad_a.color("white")
pad_a.shapesize(stretch_wid=5, stretch_len=1)
pad_a.penup()
pad_a.goto(-350, 0)

#poddle B
pad_b = turtle.Turtle()
pad_b.speed(0)
pad_b.shape("square")
pad_b.color("white")
pad_b.shapesize(stretch_wid=5, stretch_len=1)
pad_b.penup()
pad_b.goto(350, 0)

#bola
bola = turtle.Turtle()
bola.speed(0)
bola.shape("square")
bola.color("white")
bola.penup()
bola.goto(0, 0)

#funções
def pad_a_up():
    y = pad_a.ycor()
    y += 20
    pad_a.sety(y)
def pad_a_down():
    y = pad_a.ycor()
    y -= 20
    pad_a.sety(y)

def pad_b_up():
    y = pad_b.ycor()
    y += 20
    pad_b.sety(y)
def pad_b_down():
    y = pad_b.ycor()
    y -= 20
    pad_b.sety(y)

#keyboard binding
wn.listen()
wn.onkeypress(pad_a_up, "w")
wn.onkeypress(pad_a_down, "s")
wn.onkeypress(pad_b_up, "Up")
wn.onkeypress(pad_b_down, "Down")

#velocidade da bola
bola.dx = 0.2
bola.dy = 0.2

#game loop
while True:
    wn.update()

    #movimento da bola
    bola.setx(bola.xcor() + 0.2)
    bola.sety(bola.ycor() + 0.2)


    #borda
    if bola.ycor() > 280:
        bola.sety(280)
        bola.dy *= -1
    
    if bola.ycor() < -280:
        bola.sety(-280)
        bola.dy *= -1
    
    if bola.xcor() > 390:
        bola.setx(390)
        bola.goto(0, 0)
        bola.dx *= -1
    
    if bola.xcor() < -390:
        bola.setx(-390)
        bola.goto(0, 0)
        bola.dx *= -1