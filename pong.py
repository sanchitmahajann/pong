#Simple pong game
import turtle
import winsound

win = turtle.Screen()               #the actual window
win.title('Pong by Sanchit')
win.bgcolor('Black')
win.setup(width=800, height=600)
win.tracer(0)                       #prevents auto-update

#Score A
score_a = 0
score_b = 0

#Paddle L
paddle_l = turtle.Turtle()
paddle_l.speed(0)
paddle_l.shape('square')            #20pix x 20pix size
paddle_l.shapesize(stretch_wid=5, stretch_len=1)
paddle_l.color('White')
paddle_l.penup()
paddle_l.goto(-350,0)


#Paddle R
paddle_r = turtle.Turtle()
paddle_r.speed(0)
paddle_r.shape('square')            #20pix x 20pix size
paddle_r.shapesize(stretch_wid=5, stretch_len=1)
paddle_r.color('White')
paddle_r.penup()
paddle_r.goto(350,0)


#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')            #20pix x 20pix size
ball.color('white')
ball.penup()
ball.goto(0,0)
ball.dx = 0.35
ball.dy = -0.35

#UI ans Scoreboard
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write('Player A: 0 & Player B: 0', align='center', font=("Segoe UI", 24, "bold"))


#Functions to move paddles
def paddle_l_up():
    y = paddle_l.ycor()
    y += 20
    paddle_l.sety(y)

def paddle_l_down():
    y = paddle_l.ycor()
    y -= 20
    paddle_l.sety(y)

def paddle_r_up():
    y = paddle_r.ycor()
    y += 20
    paddle_r.sety(y)

def paddle_r_down():
    y = paddle_r.ycor()
    y -= 20
    paddle_r.sety(y)


#Keybinds
win.listen()
win.onkeypress(paddle_l_up, 'w')
win.onkeypress(paddle_l_down, 's')

win.onkeypress(paddle_r_up, 'Up')
win.onkeypress(paddle_r_down, 'Down')


#Game Loop
while True:
    win.update()
    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -285:
        ball.sety(-285)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if paddle_l.ycor() > 248:
        paddle_l.sety(248)

    if paddle_l.ycor() < -248:
        paddle_l.sety(-248)

    if paddle_r.ycor() > 248:
        paddle_r.sety(248)

    if paddle_r.ycor() < -248:
        paddle_r.sety(-248)

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write('Player A: {} & Player B: {}'.format(score_a, score_b), align='center', font=("Segoe UI", 24, "bold"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write('Player A: {} & Player B: {}'.format(score_a, score_b), align='center', font=("Segoe UI", 24, "bold"))

    #Can-Collide to On
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_r.ycor() + 40 and ball.ycor() > paddle_r.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_l.ycor() + 40 and ball.ycor() > paddle_l.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)