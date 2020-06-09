# python 3.5

# press 0 to see speed
# press 4 to see wheel/acc/break

from gym_torcs import TorcsEnv
import numpy as np
import math

step = 0

# Generate a Torcs environment
env = TorcsEnv()


def station_control(ob):
    target_speed = 10
    speed = math.sqrt(ob.speedX * ob.speedX + ob.speedY * ob.speedY)
    print('speedX:', ob.speedX,'angle:', ob.angle)
    if ob.speedX > target_speed:
        accel = 0
    else:
        accel =1
    brake = 0
    return accel, brake


def lateral_control(ob):
    return 0.1


for i in range(10000):
    print("Episode : " + str(i))

    if np.mod(i, 3) == 0:
        ob = env.reset(relaunch=True)
    else:
        ob = env.reset()

    for j in range(10000):
        accel, brake = station_control(ob)
        steer = lateral_control(ob)
        action = {'steer': steer, 'accel': accel, 'brake': brake}
        print(str(j) + ' ' + str(action))
        ob = env.step(action)

env.end()  # This is for shutting down TORCS
