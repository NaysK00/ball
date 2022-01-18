from panda3d.core import *
from  direct.showbase.ShowBase import ShowBase
from direct.task import Task
from math import sin, pi

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        self.setBackgroundColor(0,0,0)
        self.model = self.loader.loadModel("ball.dae")
        self.model.reparentTo(self.render)
        box =self.model.getTightBounds()
        # print(box)
        self.model.setPos(-(box[0][0] + box[1][0]) / 2, -(box[0][1] + box[1][1]) / 2, -(box[0][2] + box[1][2]) / 2)
        self.ball = self.render.attachNewNode("ball")
        self.model.reparentTo(self.ball)
        self.ball.reparentTo(self.render)
        self.ball.setY(17.5)
        spotlight = Spotlight("spotlight")
        self.spot = self.render.attachNewNode(spotlight)
        self.spot.setPos(-25, -15, 30)
        self.spot.lookAt(self.ball)
        self.render.setLight(self.spot)
        ambientLight = AmbientLight("ambientLight")
        ambientLight.setColor((0.1, 0.1, 0.1, 1))
        self.ambient = self.render.attachNewNode(ambientLight)
        self.render.setLight(self.ambient)

        self.ball.setHpr(90, -60, 0)

        self.grid = self.loader.loadModel("the_grid/scene.gltf")
        self.grid.reparentTo(self.render)
        self.grid.setScale(0.005)
        self.grid.setY(2)
        self.grid.setZ(15)
        self.grid.setX(-18.3077 / 2)

        # self.spot.node().setShadowCaster(True, 8192, 8192)
        # self.render.setShaderAuto()
        # self.render.setDepthOffset(-3)

        self.taskMgr.add(self.spin, "SpinTask")

    def spin(self, task):
        angle = task.time*72
        self.ball.setR(angle)
        direction = int(task.time //2.5)%2
        if direction:
            x = task.time %2.5*4-5
        else:
            x = 5-task.time % 2.5*4

        self.ball.setX(x)
        angle = task.time*72*(direction*2-1)

        z = sin(task.time*2 %pi)*4.75 - (3.30781-1.6)
        self.ball.setZ(z)
        return Task.cont




app = MyApp()
app.run()
