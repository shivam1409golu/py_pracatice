import turtle

t = turtle.Turtle()
t.speed(5)

# Sun
t.penup()
t.goto(200,200)
t.pendown()
t.circle(40)

# House body
t.penup()
t.goto(-50,-50)
t.pendown()

for i in range(4):
    t.forward(150)
    t.left(90)

# Roof
t.left(45)
t.forward(106)
t.left(90)
t.forward(106)
t.left(45)

# Door
t.penup()
t.goto(10,-50)
t.pendown()

t.setheading(90)
t.forward(70)
t.right(90)
t.forward(40)
t.right(90)
t.forward(70)

# Tree trunk
t.penup()
t.goto(-150,-50)
t.pendown()

t.setheading(90)
t.forward(80)

# Tree leaves
t.penup()
t.goto(-150,50)
t.pendown()
t.circle(40)

turtle.done()
