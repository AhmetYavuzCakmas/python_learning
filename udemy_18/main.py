from turtle import Turtle,Screen
tim = Turtle()
screen = Screen()

def ileri():
    tim.forward(10)

def right():
    new_heading = tim.heading() + 30
    tim.setheading(new_heading)

def left():
    new_heading = tim.heading() -30
    tim.setheading(new_heading)

def back():
    tim.backward(10)

def clear():
    tim.clear()
    tim.penup() #kalemin çizim yapmadan hareket etmesini sağlar
    tim.home()
    tim.pendown()#kalem tekrar çizim yapmaya başlar.


screen.onkey(ileri,"w")
screen.onkey(right,"d")
screen.onkey(left,"a")
screen.onkey(back,"s")
screen.onkey(clear,"c")


screen.listen()
screen.exitonclick()
