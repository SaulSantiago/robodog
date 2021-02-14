from controller import Robot
'''

'''
dog: Robot = Robot()
timeStep: int = int(dog.getBasicTimeStep())
motors: dict = {
    "head": {
        "vertical":dog.getDevice("PRM:/r1/c1-Joint2:11"),
        'horizontal': dog.getDevice('PRM:/r1/c1/c2-Joint2:12'),
    }
}

motorx = 0
motory = 0
lookingUp = True
lookspeed = 0.001
while dog.step(timeStep) != -1:
    lookingUp = motorx >= motors['head']['vertical'].getMaxPosition()
    if lookingUp:
        motorx += lookspeed
    else:
        motorx -= lookspeed
    motors['head']['vertical'].setPosition(motorx)