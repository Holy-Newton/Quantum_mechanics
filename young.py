#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  2 16:17:33 2025

@author: francoisdeberdt
"""

import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
import statistics
from scipy.integrate import solve_ivp
from matplotlib.animation import FuncAnimation
import random

fig = plt.figure()
ax = plt.subplot()

fig.patch.set_facecolor('black')
ax.set_facecolor('black')

size_x = 12000
size_y = 20
ax.set_xlim(-size_x, size_x)
ax.set_ylim(-size_y, size_y)


A=30
d = 1e-4
L = 0.550
lamb = 600e-9
k = 2*np.pi/lamb
fps = 160
nbr_f=3000

X_val = np.linspace(-size_x, size_x, 1000)
I_val = A**2 *(1 +np.cos(k *d *X_val /L))

I_val_n =I_val/np.sum(I_val)

def aleat_x():
    return np.random.choice(X_val, p=I_val_n)

scattation = ax.scatter([],[], s=4, c='yellow')
x, y = [], []

def update(fps):
    global x, y
    n_x = aleat_x()
    n_y = np.random.uniform(-size_y, size_y)
    
    x.append(n_x)
    y.append(n_y)
    
    scattation.set_offsets(np.column_stack(([x,y])))
    return scattation,

ani = FuncAnimation(fig, update, frames =nbr_f, interval=fps, blit=False)
ax.set_title('-----  I(x) = E(x)^2  -----', color='white')
plt.show()






