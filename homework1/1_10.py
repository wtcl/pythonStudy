import turtle as t

t.speed(100)
t.pensize(2)
t.bgcolor('black')
colors=['red', 'yellow', 'purple', 'blue']
t.tracer(False)
for x in range(400):
    t.forward(2*x)
    t.color(colors[x %4])
    t.left(91)
t.tracer(True)
t.done()
