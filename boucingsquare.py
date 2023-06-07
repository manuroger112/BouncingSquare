import turtle
import random





turtle.setup(800, 600)


turtle.speed(0)
turtle.hideturtle()
turtle.colormode(255)


#TEXT

text = turtle.Turtle();
text.speed(0)
text.hideturtle()
text.penup
text.goto(0, 200)
text.color("white")
text.hideturtle()
text.write('Please press Q to quit the program', font="Arial", align='center')

#WINDOW

w = turtle.Screen()
w.bgcolor("black")

#BORDER

brd = turtle.Turtle()
brd.width(5)
brd.speed(0)
brd.shape("square")
brd.penup()
brd.color("white")
brd.goto(300,300)
brd.pendown()
brd.pencolor("white")

    
brd.backward(600)
brd.right(90)
brd.forward(600)
for x in range(2):
    brd.left(90)
    brd.forward(600)

brd.hideturtle()


def RandomColors():
    R = random.randint(0,255)
    G = random.randint(0,255)
    B = random.randint(0,255)

    t.color(R, G, B)
    
def exitprogram():
    
    
    turtle.bye()





#SQUARE

t = turtle.Turtle()

t.shape("square")
t.color("white")
t.penup()
t.shapesize(stretch_wid=3, stretch_len=3)


#VELOCITY

xVel = 3
yVel = 2


#PHYSICS

while True:
    
    xt = t.xcor() 
    yt = t.ycor()
    print(xt," ", yt)
    
    

    if xt >= 300 - 30 or xt <= -300 + 30:
        
        xVel *= -1
        RandomColors();



    if yt >= 300 - 30 or yt <= -300 + 30:
        
        yVel *= -1
        RandomColors();
        
    turtle.listen()

    turtle.onkey(exitprogram, "q" or "Q")

   
        
        
    
    
    
        


    xt += xVel
    yt += yVel
    t.goto(xt , yt )

    

    
  




