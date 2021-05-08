import turtle
def tree_leaves(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.setheading(0)
    turtle.color('red')
    turtle.begin_fill()
    turtle.forward(40)
    turtle.left(120)
    turtle.forward(40)
    turtle.left(120)
    turtle.forward(40)
    turtle.end_fill()
def tree_trunk(x, y):
    turtle.penup()
    turtle.goto(x+12.5, y)
    turtle.pendown()
    turtle.color('green')
    turtle.begin_fill()
    turtle.setheading(0)
    turtle.forward(15)
    turtle.right(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(15)
    turtle.right(90)
    turtle.forward(25)
    turtle.end_fill()
tree_leaves(0,0)
tree_leaves(0,20)
tree_leaves(0,40)
tree_trunk(0,0)