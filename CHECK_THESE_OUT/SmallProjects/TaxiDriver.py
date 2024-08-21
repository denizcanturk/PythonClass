#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 24 13:20:36 2022

@author: debinci
"""
import gym                                          
import numpy as np                                  
import random
# Visualizing Helper 
from IPython.display import display, clear_output   
from time import sleep

RANDOM_ACTION_COUNT = 100
SLEEP_FOR = 0.2
PREVIEW_COUNT = 5

# hyperparameters
learning_rate = 0.9
discount_rate = 0.8
epsilon = 1.0
decay_rate= 0.005

# Iteration Counts
TRAINING_ITERATION_COUNT = 5000
MAX_TRIAL_NUMBER = 99
max_steps = 99 # per episode in case of unsuccess

# create env and reset it to state-O
env = gym.make('Taxi-v3')
state = env.reset()

print(f"Initial state: {state}")

for s in range(RANDOM_ACTION_COUNT+1):

    clear_output(wait=True) 

    print(f"Step: {s} / {RANDOM_ACTION_COUNT}")

    # Choose the random action
    action = env.action_space.sample()

    # Act like a Pro
    env.step(action)

    # Show Fancy Results
    env.render()

    sleep(0.2)

# Time to Kill the Environment
env.close()

class bcolors:
    RED= '\u001b[31m'
    GREEN= '\u001b[32m'
    RESET= '\u001b[0m'

# create Taxi environment
env = gym.make('Taxi-v3')

# initialize q-table
state_size = env.observation_space.n
action_size = env.action_space.n
qtable = np.zeros((state_size, action_size))

print("TRAINING IN PROGRESS...")

for episode in range(TRAINING_ITERATION_COUNT):

    # Reset the environment at each iteration
    state = env.reset()
    step = 0
    done = False
    
    for step in range(MAX_TRIAL_NUMBER):

        # Exploration-Exploitation Decision
        if random.uniform(0,1) < epsilon:
            # Explore
            action = env.action_space.sample()
        else:
            # Exploit
            action = np.argmax(qtable[state,:])

        # Take an action and observe the reward
        new_state, reward, done, info = env.step(action)
        print(reward)
        # Collect and Keep the Rewards so we can create some fancy graphs

        # Our Fancy Q-learning algorithm
        qtable[state,action] = qtable[state,action] + learning_rate * (reward + discount_rate * np.max(qtable[new_state,:])-qtable[state,action])

        # Update to our new state
        state = new_state

        # if done, finish episode
        if done == True:
            break

    # Decrease epsilon exponantially
    epsilon = np.exp(-decay_rate*episode)
    
# Get ready to watch our trained agent
clear_output()
print(f"Q-table Looks Like    : {qtable}")
print(f"Training Completed In :{TRAINING_ITERATION_COUNT} episodes")

# Clear the screen and Go
clear_output()  
successCount = 0
for episode in range(PREVIEW_COUNT):

        # Reset the environment
    state = env.reset()
    step = 0
    done = False
    episode_rewards = 0

    for step in range(RANDOM_ACTION_COUNT):
        # clear screen on each iteration so we can see what's going on...
        clear_output(wait=True)

        print(f"TAXI IN ACTION")
        print(f"GAME : {episode+1}")
        print(f"Step : {step+1}")
        if episode_rewards < 0:
            print(f"Score: {bcolors.RED}{episode_rewards}{bcolors.RESET}")
        else:
            print(f"Score: {bcolors.GREEN}{episode_rewards}{bcolors.RESET}")

     

        
        # Exploit
        action = np.argmax(qtable[state,:])

        # Take an action and observe the reward
        new_state, reward, done, info = env.step(action)

        
        # Accumulate our rewards    
        episode_rewards += reward

 
        env.render()
        #Printing the Scores for Fancy View
        sleep(SLEEP_FOR) 
        # Update to our new state
        state = new_state

        # if done, finish episode
        if done == True:
            break  

# Close the Taxi Door
env.close()







