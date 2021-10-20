import turtle
t = turtle.Pen()
turtle.bgcolor("black")
colors = ["red", "yellow"]
t.speed(0)
sides = 2
for x in range(200):
    t.pencolor(colors[x % sides])
    t.left(360 / sides + 1)
    t.forward(x * 3 / sides + x)