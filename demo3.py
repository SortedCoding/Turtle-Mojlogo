import turtle as t

t.speed(2)
t.width(2)

def relative_pos(x, y):
    t.penup()
    t.goto(t.pos() + (x, y))
    t.pendown()

# Drawing the yellow part of the logo
t.begin_fill()
t.color('#ffab00')
for i in range(4):
    t.forward(100)
    t.circle(100, 90)
t.end_fill()

# Drawing the black part of the logo
relative_pos(140, 70)
t.seth(90)
t.color('#000')
t.begin_fill()
for i in range(3):
    if i == 1:
        t.forward(169.71)
    else:
        t.forward(120)
    t.circle(10, 135)
t.end_fill()

# Drawing the inner pattern
relative_pos(-180, 40)
t.seth(90)
t.width(20)
for i in range(4):
    t.forward(60)
    if i == 1:
        t.left(90)
    else:
        t.right(90)

t.hideturtle()
t.done()
