import turtle

win = turtle.Screen()
win.setup(0.5, 0.5)
win.bgcolor(0.2, 0.2, 0.2)
win.title("Drawing thing")


#                       !!!!USE SETHEADING!!!!
#   0   = Right
#   90  = Up
#   180 = Left
#   270 = Down
# memang can be used to alter direction... memang 90 gives 0 = Up
#pen down, point to angle and draw distance
def draw(angle, distance, shift):
    #anglee = memang
    #if anglee > angle:
    #    diff = anglee - angle
    #    if diff > 180:
    #        diff = diff - 180
    #        turtle.left(diff)
    #    else:
    #        turtle.right(diff)
    #elif angle > anglee:
    #    diff = angle - anglee
    #    if diff > 180:
    #        diff = diff - 180
    #        turtle.right(diff)
    #    else:
    #        turtle.left(diff)
    #SETHEADING does all of the above.
    turtle.setheading(angle + shift)
    turtle.pendown()
    turtle.forward(distance)      
#pen up, point to angle and move distance
def move(angle, distance):
    #anglee = memang
    #if anglee > angle:
    #    diff = anglee - angle
    #    if diff > 180:
    #        diff = diff - 180
    #        turtle.right(diff)
    #    else:
    #        turtle.left(diff)
    #elif angle > anglee:
    #    diff = angle - anglee
    #    if diff > 180:
    #        diff = diff - 180
    #        turtle.left(diff)
    #    else:
    #        turtle.right(diff)
    #SETHEADING does all of the above.
    turtle.setheading(angle)
    turtle.penup()
    turtle.forward(distance)
#choose style of pen
def style(color, size, speed):
    turtle.color(color)
    turtle.speed(speed)
    turtle.pensize(size)

#draw a circle: verts = amount of vertices, dia = Diameter
def draw_shape(verts, dia):
    mem = 90
    dang = 0
    circ = dia * 3.1415
    versize = circ / verts
    for i in range(verts):
        dang = mem + (360 / verts)

        draw(dang, versize)
        mem = dang
        #move(0, 0)   
        i + 1 

def draw_flower(petals, size):
    st = 0
    pang = 360 / petals
    for i in range(petals):
        ping = st * pang
        draw_shape(300, size)
        
style('yellow', 1, 150)

draw_flower(8, 200)

turtle.done()