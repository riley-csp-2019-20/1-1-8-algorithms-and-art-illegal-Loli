import turtle as trtl

crown = trtl.Turtle()
crown.speed(5)
#making the crown and coloring it yellow
crown.pencolor("yellow")
crown.fillcolor("yellow")
crown.begin_fill()
crown .forward(100)
crown .left(90)
crown .forward(80)
crown .left(40)
crown .forward(40)
crown .left(100)


crown .forward(40)
crown .right(100)
crown .forward(40)
crown .left(100)
crown .right(100)
crown .forward(40)
crown .left(100)

crown .forward(40)


crown .forward(40)

crown .right(100)
crown .forward(40)
crown .left(90)

crown .forward(40)
crown .left(50)
crown .forward(85)
crown .left(90)
crown .forward(110)
crown.end_fill()





# makeing jewel1 red
crown.pencolor("red")
crown.fillcolor("red")
crown.begin_fill()
crown.penup()
crown.goto(-5,115)
crown.pendown()
crown.left(250)
crown.forward(63)
crown.left(70)
crown.forward(30)
crown.left(80)
crown.forward(30)
crown.left(70)
crown.forward(68)
crown.end_fill()


#making jewel2 red
crown.penup()
crown.goto(-80,75)
crown.pencolor("red")
crown.fillcolor("red")
crown.begin_fill()
crown.left(130)
crown.forward(35)
crown.left(80)
crown.forward(25)
crown.left(80)
crown.forward(25)
crown.left(80)
crown.forward(41)
crown.end_fill()

#making the last jewel on the right
crown.penup()
crown.goto(70,75)
crown.pendown()
crown.pencolor("red")
crown.fillcolor("red")
crown.begin_fill()
crown.left(120)
crown.forward(35)
crown.left(80)
crown.forward(25)
crown.left(80)
crown.forward(25)
crown.left(80)
crown.forward(41)
crown.end_fill()

#outline of icekings face
import turtle as trtl

iced = trtl.Turtle()
iced.speed(5)
iced.penup()
iced.goto(-110,0)
iced.pendown()
iced.right(105)
iced.forward(130)
iced.left(60)
iced.forward(130)
iced.penup()
iced.goto(105,0)
iced.pendown()
iced.left(-30)
iced.forward(130)
iced.right(60)
iced.forward(130)


#ice kings blue face
iced.penup()
iced.goto(-80,0)
iced.pendown()
iced.pencolor("blue")
iced.fillcolor("blue")
iced.begin_fill()
iced.left(30)
iced.forward(100)
iced.left(120)
iced.forward(80)
iced.right(90)
iced.forward(90)
iced.left(140)
iced.forward(95)
iced.right(80)
iced.forward(80)
iced.left(120)
iced.forward(100)
iced.end_fill()
#while loop required so i did it with eyes.
#i also tried making it appear as if he was blinking and looking to
#the left from the left

import turtle as trtl

eyes = trtl.Turtle()
eyes.speed(0)
eye = 0

while (eye < 1):
  eyes.pencolor("white")
  eyes.fillcolor("white")
  eyes.begin_fill()
  eyes.penup()
  eyes.goto(-40,-60)
  eyes.pendown()
  eyes .circle(20,360,)
  eyes.end_fill()

  eye += 1

eye2 = 0

while (eye2 < 1):    
    eyes.pencolor("white")
    eyes.fillcolor("white")
    eyes.begin_fill()
    eyes.penup()
    eyes.goto(20,-60)
    eyes.pendown()
    eyes .circle(20,360,)
    eyes.end_fill() 

    eye2 += 1



eye3 = 0

while (eye3 < 1):
  eyes.pencolor("blue")
  eyes.fillcolor("blue")
  eyes.begin_fill()
  eyes.penup()
  eyes.goto(-40,-60)
  eyes.pendown()
  eyes .circle(20,360,)
  eyes.end_fill()

  eye3 += 1




eye4 = 0

while (eye4 < 1):    
    eyes.pencolor("blue")
    eyes.fillcolor("blue")
    eyes.begin_fill()
    eyes.penup()
    eyes.goto(20,-60)
    eyes.pendown()
    eyes .circle(20,360,)
    eyes.end_fill() 

    eye4 += 1



eye5 = 0

while (eye5 < 1):
  eyes.pencolor("white")
  eyes.fillcolor("white")
  eyes.begin_fill()
  eyes.penup()
  eyes.goto(-20,-60)
  eyes.pendown()
  eyes .circle(20,360,)
  eyes.end_fill()

  eye5 += 1


eye6 = 0

while (eye6 < 1):    
    eyes.pencolor("white")
    eyes.fillcolor("white")
    eyes.begin_fill()
    eyes.penup()
    eyes.goto(60,-60)
    eyes.pendown()
    eyes .circle(20,360,)
    eyes.end_fill() 

    eye6 += 1


wn = trtl.Screen()
wn.mainloop()
