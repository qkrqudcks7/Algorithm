import turtle as t
import random as r

for i in range(100):
    x = r.randrange(1, 201)
    y = r.randrange(1, 201)

    t.pendown()
    t.goto(x, y)