import turtle 

name = ["mohammad","ahmad" ,"mobin", "ali"]
position = [(100,40) , (150,200),(24,46),(56,100)]


screen = turtle.Screen()
screen.bgcolor(input(":"))
t = turtle.Turtle()
for i in range(4) : 
    t.hideturtle
    t.penup()
    t.goto(position[i])
    t.pendown() 
    t.color(input(":"))
    t.write(name[i] , font=("arial",16,"normal",))
t.hideturtle()  








turtle.done()