import turtle
t=turtle.Pen()

while True:
    direction=input("왼쪽=left 오른쪽은=right")
    if direction=="left":
        t.left(60)
        t.forward(50)
    else:
        if direction=="right":
            t.right(60)
            t.forward(50)
