import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500,500)
user_bahis = screen.textinput(title="tahmin yap",prompt="hangi renk kaplumbağ kazanır? : ")
print(user_bahis)

turtle_list = ["red","orange","yellow","green","blue","purple"]
y_positions = [150,100,50,0,-50,-100]
all_turtles = []
"""
a = 150
for i in turtle_list:
    tim = Turtle(shape="turtle")
    tim.color(i)
    tim.penup()
    tim.goto(x=-230, y=a)
    a -= 50
"""
is_race_on = False

for i in range(0,6):
    new_turtles = Turtle(shape="turtle")
    new_turtles.color(turtle_list[i])
    new_turtles.penup()
    new_turtles.goto(x=-230, y=y_positions[i])
    all_turtles.append((new_turtles))

if turtle_list:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>200:
            is_race_on = False
            kazanan_renk = turtle.pencolor()
            if kazanan_renk == user_bahis:
                print(f"kazandınız. {kazanan_renk} kaplubmağa kazanıd")
            else:
                print(f"kaybettiniz.  {kazanan_renk} kaplumbağa kazandı")


        rastgele_hız = random.randint(1,10)
        turtle.forward(rastgele_hız)









screen.exitonclick()
