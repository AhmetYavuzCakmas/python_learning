import turtle as t
from turtle import Screen
import random

tim = t.Turtle()
tim.shape("turtle")
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color

angle = 15
tim.pensize(2)
tim.speed("fastest")
angle_kullanıcı = int(input("yarıçap giriniz: "))
#while (angle<360):
for _ in range(1000):
    tim.right(100)
    tim.circle(angle_kullanıcı)
    tim.color(random_color())
    angle += 15 + angle




screen= t.Screen()
screen.exitonclick()