import turtle as t

t.speed(100)
t.pensize(2)
colors = ["red", "green", "blue","yellow"]
for x in range(100):
    t.pencolor(colors[x %4])
    t.forward(2*x)
    t.left(90)
t.exitonclick()
