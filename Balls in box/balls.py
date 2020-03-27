from vpython import *
import numpy as np

scene=canvas(width=800, height=800)
wallL=box(canvas=scene, pos=vec(-5.5, 0, 0), size=vec(1, 10, 10), color=color.red)
wallR=box(canvas=scene, pos=vec(5.5, 0, 0), size=vec(1, 10, 10), color=color.blue)
wallB=box(canvas=scene, pos=vec(0, 0, -5.5), size=vec(10, 10, 1), color=color.yellow)
wallC=box(canvas=scene, pos=vec(0, 5.5, 0), size=vec(10, 1, 10), color=color.green)
wallF=box(canvas=scene, pos=vec(0, -5.5, 0), size=vec(10, 1, 10), color=color.magenta)

N=count=10
L=[]
for i in range(-3, 4):
    for j in range(-3, 4):
        if count>0:
            L.append(sphere(canvas=scene, pos=vec(i, j, 0), radius=0.4))
        count=count-1

for i in L:
    i.vel = vec(np.random.uniform(0, 1, 1), np.random.uniform(0, 1, 1), np.random.uniform(0, 1, 1))

t=0
dt=0.05
while t<100:
    rate(100)
    for i in L:
        i.pos = i.pos + i.vel * dt
        if i.pos.x <= -4 or i.pos.x >= 4:
            if i.pos.x < 0:
                i.vel.x = -i.vel.x
                i.color = color.red
            else:
                i.vel.x = -i.vel.x
                i.color = color.blue
        if i.pos.y <= -4 or i.pos.y >= 4:
            if i.vel.y < 0:
                i.vel.y = -i.vel.y
                i.color = color.magenta
            else:
                i.vel.y = -i.vel.y
                i.color = color.green
        if i.pos.z <= -4 or i.pos.z >= 4:
            if i.pos.z < 0:
                i.vel.z = -i.vel.z
                i.color = color.yellow
            else:
                i.vel.z = -i.vel.z
                i.color = color.white
    for i in range(0, N):
        for j in range(i+1, N):
            if sqrt((L[i].pos.x-L[j].pos.x)**2+ (L[i].pos.y-L[j].pos.y)**2 +(L[i].pos.z-L[j].pos.z)**2)<0.8:
                temp=L[i].vel
                L[i].vel=L[j].vel
                L[j].vel=temp
    t = t + dt
