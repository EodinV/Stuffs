import turtle

win = turtle.Screen()
win.setup(0.75, 0.75)
win.bgcolor(0.6, 0.6, 0.6)
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
def draw_shape(verts, dia, shift):
    mem = 90
    dang = 0
    circ = dia * 3.1415
    versize = circ / verts
    for i in range(verts):
        dang = mem + (360 / verts)

        draw(dang, versize, shift)
        mem = dang
        #move(0, 0)   
        i + 1 



#Stoverride is to lock style to whatever is set outside function.
def draw_flower(petals, size, stoverride):
    pang = 360 / petals
    ping = 0
    vert = petals * 2
    ding = size / (petals/2)
    color = 0
    for i in range(petals):
        draw_shape(vert, size, ping)
        ping = ping + pang
        move(ping, ding)
        color += 1
        if stoverride == 0:
            if color == 0:
                style('black', 1, 10)
            elif color == 1:
                style('gray', 1, 10)
            elif color == 2:
                style('red', 1, 10)
            elif color == 3:
                style('orange', 1, 10)  
            elif color == 4:
                style('yellow', 1, 10)
            elif color == 5:
                style('green', 1, 10)
            elif color == 6:
                style('blue', 1, 10)
            elif color == 7:
                style('purple', 1, 10)
            elif color == 8:
                style('red', 1, 10)
            elif color == 9:
                style('white', 1, 10)

            if color > 9:
                color = 0

        
        



draw_flower(64, 200, 0)

turtle.done()