# 1

A = 1
B = 2
C = 3
D = 4

print(A + B)
print(A * B)
print (B - A)

print (C + D)
print(C * D)
print(D - C)


# 2



from turtle import *
# start square we need to draw 3 sqare 
speed(90000)
color('yellow')
forward(300)
begin_fill()
right(90)
forward(300)
right(90)
forward(300)
right(90)
forward(300)
right(90)
end_fill()
#start second square
begin_fill()
right(90)
forward(300)
right(90)
forward(200)
right(90)
forward(200)
right(90)
forward(200)
end_fill()
#start the third wall
penup()
goto(0, - 300)
pendown()
forward(500)
begin_fill()
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
right(90)
end_fill()
#start the door
forward(200)
color('green')
begin_fill()
right(90)
forward(100)
right(90)
forward(50)
right(90)
forward(100)
end_fill()
#start windows
penup()
goto(90,-100)
pendown()
#start windows
color('blue')
begin_fill()
forward(100)
right(90)
forward(100)
right(90)
forward(90)
right(90)
forward(100)
end_fill()
#second window but before...
color('yellow')
forward(80)
#start window :}
color('blue')
begin_fill()
forward(90)
right(90)
forward(90)
right(90)
forward(90)
right(90)
forward(90)
right(90)
end_fill()
#start  roofs
penup()
goto(00,00)
pendown()
#start with color
color('black')
begin_fill()
forward(300)
left(120)
forward(300)
left(120)
forward(300)
end_fill()
#start the flag
penup()
goto(00,00)
pendown()
#start

left(125)
forward(150)
left(90)
forward(300)
right(90)
forward(80)
right(90)
forward(90)
left(90)
forward(80)
left(90)
forward(80)
left(90)
forward(80)
left(90)
forward(60)
left(90)
forward(20)
right(180)
right(90)




exitonclick()