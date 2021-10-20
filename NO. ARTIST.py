import turtle
t = turtle.Pen()
turtle.bgcolor("black")
t.speed(0)
colors = ['red', 'yellow', 'green', 'blue', 'orange', 'purple', 'silver', 'pink', 'navy', 'white']
side = int(turtle.numinput("Choose the sides", "Enter the sides you want between 2 - 10 (remember dont chose side 1)"))
for x in range(200):
    t.pencolor(colors[x % side])
    t.forward(x * 3 / side + x)
    t.left(360 / side + 1)
