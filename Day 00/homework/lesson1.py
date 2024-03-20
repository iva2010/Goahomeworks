from turtle import *
forward (200)
# we want to paint a house
#step 1: draw a square

speed(30)

left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
width(7)
color("purple")
#end of square

#drawing a door
forward(70)
color("green")
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
begin_fill()
#end of door

penup()
goto(200,200)
pendown()
color("red")

begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill() 
#end of door


#draw two windows
penup()
goto(170, 180)
pendown()
color("blue")

begin_fill()
right(60)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()

penup()
goto(70, 180)
pendown()

begin_fill()
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()

exitonclick()