# python 3.5

from gym_torcs import TorcsEnv
from sample_agent import Agent
import numpy as np

episode_count = 10
max_steps = 50
reward = 0
done = False
step = 0

# Generate a Torcs environment
env = TorcsEnv(throttle=True)



print("TORCS Experiment Start.")
for i in range(episode_count):
    print("Episode : " + str(i))

    if np.mod(i, 3) == 0:
        # Sometimes you need to relaunch TORCS because of the memory leak error
        ob = env.reset(relaunch=True)
    else:
        ob = env.reset()

    for j in range(max_steps):
        print(j)
        # action = agent.act
        steer =0
        acc =0.2
        brk =0
        if j>20:
            acc=0
            brk =1
        action = np.array([steer,acc,brk])
        ob, _, done, _ = env.step(action)
        step += 1
        if done:
            break
    print("Total Step: " + str(step))

env.end()  # This is for shutting down TORCS
print("Finish.")
