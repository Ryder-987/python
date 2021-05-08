'''
請使用def畫出10個，不同顏色的屋頂、房身，及位置的房子
顏色用list用代入
'''
import turtle

color_list = ['red' , 'green' , 'yellow', 'gold' , 'brown', 'chocolate', 'orange', 'seilver' ,'pink']

import turtle
def house_roof(x, y, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.setheading(0)
    turtle.color(color)
    turtle.begin_fill()
    turtle.forward(40)
    turtle.left(120)
    turtle.forward(40)
    turtle.left(120)
    turtle.forward(40)
    turtle.end_fill()
def house_body(x, y):
    turtle.penup()
    turtle.goto(x+3, y)
    turtle.pendown()
    turtle.color('blue')
    turtle.begin_fill()
    turtle.setheading(0)
    turtle.forward(35)
    turtle.right(90)
    turtle.forward(35)
    turtle.right(90)
    turtle.forward(35)
    turtle.right(90)
    turtle.forward(35)
    turtle.end_fill()

for i in range(10):
    house_roof(-300+i*40, 0, color_list[i])
    house_body(-300+i*40, 0)