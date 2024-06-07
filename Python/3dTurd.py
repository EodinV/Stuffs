import turtle as tu
import math

win = tu.Screen()
win.setup(0.75, 0.75)
win.bgcolor(0.6, 0.6, 0.6)
win.title("The Matrix")
win.setworldcoordinates(-16, -16, 16, 16)
t = tu.Turtle()
bi = 0

cube_vertices = [(1, 1, 1), (-1, 1, 1), (-1, -1, 1), (1, -1, 1),
                 (1, 1, -1), (-1, 1, -1), (-1, -1, -1), (1, -1, -1)]

matrix = [[cube_vertices], 
          [cube_vertices],
          [cube_vertices],
          [cube_vertices]]



camera_pos = (0, 0, -10)
camera_dist = 5
camera_angle = 45 #Angle is from straight into cube.

def perspective(vertex, camera_distance, camera_angle):
    x, y, z = vertex
    #Adjustment to camera angle
    x_rot = x * math.cos(math.radians(camera_angle))
    z_rot = z * math.sin(math.radians(camera_angle))
    #2D ---> 3D-Projection
    x_proj = x_rot * camera_distance / (camera_distance + z_rot)
    y_proj = y * camera_distance / (camera_distance + z_rot)

    return x_proj, y_proj




def wait_key():
    tu.Screen().onkey(tu.bye, 'q')
    tu.listen()
    tu.mainloop()

for i in matrix:
    bi + .25
    for vertex in cube_vertices:
        x_proj, y_proj = perspective(vertex, camera_dist, camera_angle)
        t.penup()
        t.goto(x_proj + bi, y_proj + bi)
        t.dot(5)


wait_key()