import random as r
import time as ti
import turtle as t

#Space invade using Turtle... with help.

FRAME_RATE = 30
TIME_FOR_1_FRAME = 1 / FRAME_RATE

CANNON_STEP = 7
LAZ_LENGTH = 20
LAZ_SPEED = 20
AL_SPAWN_INTEVAL = 1.2 #secs
AL_SPEED = 3.5

win = t.Screen()
win.tracer(0)
win.setup(0.5, 0.75)
win.bgcolor(0.2, 0.2, 0.2)
win.title("Spinvadors")

LEFT = -win.window_width() / 2
RIGHT = win.window_width() / 2
TOP = win.window_height() / 2
BOTTOM = -win.window_height() / 2
FLOOR_LEVEL = 0.9 * BOTTOM
GUTTER = 0.025 * win.window_width()

#LAZOR
cannon = t.Turtle()
cannon.penup()
cannon.color(1, 1, 1)
cannon.tilt(90)
cannon.shape("triangle")
cannon.setposition(0, FLOOR_LEVEL)
cannon.cannon_movement = 0

#TEXT
txt = t.Turtle()
txt.penup()
txt.hideturtle()
txt.setposition(LEFT * 0.8, TOP * 0.8)
txt.color(1, 1, 1)

ls = []
ass = []


#CAOONDRAW
def draw_cannon():
    cannon.clear()
    cannon.turtlesize(2.2, 1)
    cannon.stamp()
    cannon.sety(FLOOR_LEVEL + 10)
    cannon.turtlesize(1, 1.5)
    cannon.stamp()
    cannon.sety(FLOOR_LEVEL + 20)
    cannon.turtlesize(0.8, 0.3)
    cannon.stamp()
    cannon.sety(FLOOR_LEVEL)
    win.update()

def make_ass():
    al = t.Turtle()
    al.penup()
    al.turtlesize(1.5)
    al.setposition(
        r.randint(
            int(LEFT + GUTTER),
            int(RIGHT - GUTTER),
        ),
        TOP,
    )
    al.shape("turtle")
    al.setheading(-90)
    al.color(r.random(), r.random(), r.random())
    ass.append(al)

#ILIKETOMOVEITMOVEIT
def move_left():
    cannon.cannon_movement = -1
    #new_x = cannon.xcor() - CANNON_STEP
    #if new_x >= LEFT + GUTTER:
    #    cannon.setx(new_x)    
    #    draw_cannon()

def move_right():
    cannon.cannon_movement = 1
    #new_x = cannon.xcor() + CANNON_STEP
    #if new_x <= RIGHT - GUTTER:
    #    cannon.setx(new_x)    
    #    draw_cannon()

def stop_cannon_movement():
    cannon.cannon_movement = 0

def shoot():
    l = t.Turtle()
    l.penup()
    l.color(1, 0, 0)
    l.hideturtle()
    l.setposition(cannon.xcor(),cannon.ycor())
    l.setheading(90)
    l.forward(20)
    l.pendown()
    l.pensize(5)

    ls.append(l)

def mv_laz(l):
    l.clear()
    l.forward(LAZ_SPEED)
    l.forward(LAZ_LENGTH)
    l.forward(-LAZ_LENGTH)


# PRESS THESE
win.onkeypress(move_left, "Left")
win.onkeypress(move_right, "Right")
win.onkeyrelease(stop_cannon_movement, "Left")
win.onkeyrelease(stop_cannon_movement, "Right")
win.onkeypress(shoot, "space")
win.onkeypress(t.bye, "q")
win.listen()



def rm_sp(sprite, sprite_list):
    sprite.clear()
    sprite.hideturtle()
    win.update()
    sprite_list.remove(sprite)
    t.turtles().remove(sprite)


#LOOPLOOP
al_timen = 0
game_timer = ti.time()
score = 0
game_running = True

while game_running:
    
    
    
    timer_frame= ti.time()
    time_elapsed = ti.time() - game_timer
    txt.clear()
    txt.write(
        f"Time: {time_elapsed:5.1f}s\nScore: {score:5}",
        font=("Courier", 20, "bold"),
    )

    for l in ls.copy():
        mv_laz(l)
        if l.ycor() > TOP:
            rm_sp(l, ls)
            break
        for al in ass.copy():
            if l.distance(al) < 20:
                rm_sp(l, ls)
                rm_sp(al, ass)
                score += 1
                break

    new_x = cannon.xcor() + CANNON_STEP * cannon.cannon_movement
    if LEFT + GUTTER <= new_x <= RIGHT - GUTTER:
        cannon.setx(new_x)    
        draw_cannon()

    if ti.time() - al_timen > AL_SPAWN_INTEVAL:
        make_ass()
        al_timen = ti.time()
    
    for al in ass:
        al.forward(AL_SPEED)
        if al.ycor() < FLOOR_LEVEL:
            game_running = False
            break
    
    time_this_frame = ti.time() - timer_frame
    if time_this_frame < TIME_FOR_1_FRAME:
        ti.sleep(TIME_FOR_1_FRAME - time_this_frame)

    
    win.update()

splash_text = t.Turtle()
splash_text.hideturtle()
splash_text.color(0.2, 0.3, 0.6)
splash_text.write("All this base are belong to us...", font=("Times New Roman", 40, "bold"), align="center")

t.done()