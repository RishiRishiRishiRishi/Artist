import turtle
t = turtle.Pen()
turtle.bgcolor("black")
t.speed(0)
colors = ['red', 'yellow', 'green', 'blue', 'orange', 'purple', 'silver', 'pink', 'navy', 'white']
side = int(turtle.numinput("Choose the circles", "Enter the no. of circle you want between 2 - 10"))
for x in range(300):
    t.pencolor(colors[x % side])
    t.circle(x)
    t.left(360 / side + 1)