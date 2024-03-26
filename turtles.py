import turtle

#   0   = Right
#   90  = Up
#   180 = Left
#   270 = Down
# memang can be used to alter direction... memang 90 gives 0 = Up
#pen down, point to angle and draw distance
def draw(angle, distance, memang):
    anglee = memang
    if anglee > angle:
        diff = anglee - angle
        if diff > 180:
            diff = diff - 180
            turtle.left(diff)
        else:
            turtle.right(diff)
    elif angle > anglee:
        diff = angle - anglee
        if diff > 180:
            diff = diff - 180
            turtle.right(diff)
        else:
            turtle.left(diff)

    turtle.pendown()
    turtle.forward(distance)      
#pen up, point to angle and move distance
def move(angle, distance, memang):
    anglee = memang
    if anglee > angle:
        diff = anglee - angle
        if diff > 180:
            diff = diff - 180
            turtle.right(diff)
        else:
            turtle.left(diff)
    elif angle > anglee:
        diff = angle - anglee
        if diff > 180:
            diff = diff - 180
            turtle.left(diff)
        else:
            turtle.right(diff)

    turtle.penup()
    turtle.forward(distance)
#choose style of pen
def style(color, size, speed):
    turtle.color(color)
    turtle.speed(speed)
    turtle.pensize(size)

#draw a circle: verts = amount of vertices, dia = Diameter
def draw_circle(verts, dia):
    mem = 90
    dang = 0
    circ = dia * 3.1415
    versize = circ / verts
    for i in range(verts):
        dang = mem + (360 / verts)

        draw(dang, versize, mem)
        mem = dang
        #move(0, 0)   
        i + 1 


move(90, 250, 0)
move(270, 0, 0)
draw_circle(64, 2400)
draw_circle(64, 2200)
draw_circle(64, 2000)
draw_circle(64, 1800)
draw_circle(64, 1600)
draw_circle(64, 1400)
draw_circle(64, 1200)
draw_circle(64, 1000)
draw_circle(64, 800)
draw_circle(64, 600)
draw_circle(64, 400)
draw_circle(64, 200)
draw_circle(64, 100)
draw_circle(64, 50)
draw_circle(64, 25)
draw_circle(64, 12.5)





turtle.mainloop()