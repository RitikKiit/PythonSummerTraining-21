import turtle
import random 

colors = [ 'red', 'green', 'blue', 'purple', 'orange', 'salmon', 
        'cyan', 'magenta', 'yellow', 'gold', 'silver' ]

p = turtle.Pen()
p.speed(0)
for c in range(10, 610, 10):
    p.color(colors[c%11])
    for _ in range(4):
        p.forward(c)
        p.left(90)
    p.up()
    p.backward(5)
    p.right(90)
    p.forward(5)
    p.left(90)
    p.down()

turtle.exitonclick()
