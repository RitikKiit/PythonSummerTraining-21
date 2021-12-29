import turtle

p = turtle.Pen()

p.color('red', 'yellow')
p.speed(0)
p.up()
p.backward(250)
p.down()

p.begin_fill()

for _ in range(360):
    p.forward(500)
    p.left(171)

p.end_fill()

turtle.exitonclick()