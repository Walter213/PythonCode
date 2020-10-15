import turtle
colors = ['yellow', 'purple', 'red', 'orange', 'green', 'blue']
pencil = turtle.Pen()
turtle.bgcolor('black')
for x in range(360):
    pencil.pencolor(colors[x%6])
    # pencil.width(x/100 + 1) 
    pencil.width(x/100) 
    pencil.fd(x)
    pencil.left(59)
