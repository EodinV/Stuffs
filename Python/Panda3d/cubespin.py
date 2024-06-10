from direct.showbase.ShowBase import ShowBase
from panda3d.core import LRotationf, Vec3

class SpinCube(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        self.cube = self.loader.loadModel("models/cube.dae")
        self.cube.reparentTo(self.render)
        self.cube.setPos(0, 0, 0)
        self.cube.setScale(1)
        self.taskMgr.add(self.rotateCube, "rotateCube")
    
    def rotateCube(self, task):
        angle_degrees = task.time * 50
        angle_radians = angle_degrees * (3.14159 / 180.0)
        rotation = LRotationf()
        rotation.setFromAxisAngle(angle_degrees, angle_radians)
        self.cube.setQuat(rotation)
        return task.cont

app = SpinCube()
app.run()

