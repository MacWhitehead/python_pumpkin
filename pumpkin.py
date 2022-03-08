'''
Project Name: Turtle Patterns Pumpkin
Author: MacKayla Whitehead
'''
  
import turtle

def main():

    tur = turtle.Turtle()
    tur.hideturtle()
    tur.speed(0.1)


    pumpkin(tur)
    stem(tur)
    eyes(tur)
    mouth(tur)
    turtle.Screen().exitonclick()


def pumpkin(tur):
    tur.color("red")
    tur.fillcolor("orange")
    tur.begin_fill()
    tur.circle(45)
    tur.forward(40)
    tur.circle(45,180)
    tur.forward(80)
    tur.circle(45,180)
    tur.forward(40)
    tur.rt(10)
    tur.forward(50)
    tur.circle(50,180)
    tur.lt(10)
    tur.forward(60)
    tur.rt(10)
    tur.forward(50)
    tur.circle(50,180)
    tur.lt(10)
    tur.forward(45)
    tur.end_fill()


def stem(tur):
    tur.up()
    tur.goto(10,90)
    tur.down()
    tur.color('green')
    tur.fillcolor("yellow green")
    tur.begin_fill()
    tur.lt(45)
    for i in range(2):
        tur.forward(20)
        tur.lt(90)
    tur.forward(40)
    tur.end_fill()


def draw_eye(tur):
    tur.color("black")
    tur.fillcolor('yellow')
    tur.begin_fill()
    tur.lt(10)
    for i in range(2):
        tur.forward(30)
        tur.lt(120)
    tur.forward(30)
    tur.end_fill()

def eyes(tur):
    locations = [-40, 70, 40]
    for i in range(2):
        tur.up()
        tur.goto(locations[i], locations[i + 1])
        tur.down()
        draw_eye(tur)

def mouth(tur):
    tur.up()
    tur.goto(-15, 30)
    tur.down()
    tur.color("black")
    tur.fillcolor('yellow')
    tur.begin_fill()
    tur.rt(90)
    tur.circle(20, 180)
    tur.lt(90)
    tur.forward(45)
    tur.end_fill()

if __name__ == "__main__":
    main()
