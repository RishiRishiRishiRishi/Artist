import turtle
t = turtle.Pen()
turtle.bgcolor("black")
t.speed(0)
colors = ['red', 'yellow', 'green', 'blue', 'orange', 'purple', 'sea green', 'white', 'brown', 'navy']
your_name = turtle.textinput("Enter your name", "What is your name")
sides = int(turtle.numinput("Number of sides", "How many sides to want between 2-10"))
for x in range(100):
    t.pencolor(colors[x % sides % 10])
    t.penup()
    t.forward(x * 4)
    t.pendown()
    t.write(your_name, font=("Arial", int((x *2 + 4) / 4), "bold"))
    t.left(360 / sides + 2)