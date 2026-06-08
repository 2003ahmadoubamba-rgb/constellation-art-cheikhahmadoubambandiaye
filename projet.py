import turtle
import random

wn = turtle.Screen()
wn.title("Constellation de Pégase")
wn.bgcolor("black")
wn.setup(800, 600)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.penup()

etoiles = [
    (  0,  80, 13, "dakar"),
    (-120, 110, 11, "thies"),
    ( 120, 100, 10, "matam"),
    (  0,  -20, 12, "fatick"),
    (-160, -10,  8, "mbour"),
    (-210, -70,  7, "kaolack"),
    ( 160, -10,  8, "saint-louis"),
    ( 220, -90,  7, "ziguinchor"),
    ( -80,-120,  7, "louga"),
    (  60,-130,  6, "linguere"),
]

connexions = [
    (0,1),(0,2),(0,3),(1,3),(3,4),(4,5),(3,9),(9,8),(2,6),(6,7)
]

for _ in range(250):
    t.goto(random.randint(-380, 380), random.randint(-280, 280))
    t.color("white")
    t.dot(random.choice([1, 1, 2]))

for i, j in connexions:
    x1, y1 = etoiles[i][0], etoiles[i][1]
    x2, y2 = etoiles[j][0], etoiles[j][1]
    t.pencolor("gray40")
    t.pensize(1)
    t.goto(x1, y1)
    t.pendown()
    t.goto(x2, y2)
    t.penup()

for x, y, taille, nom in etoiles:
    t.goto(x, y)
    t.color("gray20")
    t.dot(taille * 3)
    t.color("gold")
    t.dot(taille)
    t.color("white")
    t.dot(taille // 2)
    t.goto(x + taille + 4, y + taille + 4)
    t.color("cyan")
    t.write(nom, font=("Arial", 8, "italic"))

t.goto(-160, 250)
t.color("white")
t.write("Constellation de Pegase", font=("Arial", 16, "bold"))

wn.mainloop()