import turtle as t

t.fillcolor("red")
t.begin_fill()
while True:
    t.forward(200)
    t.right(144)
    if abs(t.pos())<1:
        break
t.end_fill()
t.done()