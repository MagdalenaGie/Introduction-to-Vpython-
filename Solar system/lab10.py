from vpython import *
import numpy as np

scene=canvas(width=1100, height=1100)
sun=sphere(canvas=scene, pos=vec(0, 0, 0), radius=10**10, color=color.yellow)
mercury=sphere(canvas=scene, pos=vec(70*10**9, 0, 0), radius=6*10**9, color=color.white, vel=vec(0, 47*10**3, 0), make_trail=True)
venus=sphere(canvas=scene, pos=vec(110*10**9, 0, 0), radius=6*10**9, color=color.green, vel=vec(0, 35*10**3, 0), make_trail=True)
earth=sphere(canvas=scene, pos=vec(150*10**9, 0, 0), radius=6*10**9, color=color.blue, vel=vec(0, 30*10**3, 0), make_trail=True)
mars=sphere(canvas=scene, pos=vec(250*10**9, 0, 0), radius=6*10**9, color=color.red, vel=vec(0, 24*10**3, 0), make_trail=True)

def acc(planet):
    G = 6.7 * 10 ** (-11)
    Ms=2*10**30
    r=mag(planet.pos)
    a=-G*Ms/(r**3)*planet.pos
    return a


print (acc(earth))

t=0
dt=3600
while t<5*31536000:
    rate(2000)
    amerc=acc(mercury)
    mercury.vel=mercury.vel + amerc*dt
    mercury.pos=mercury.pos + mercury.vel*dt

    aven = acc(venus)
    venus.vel = venus.vel + aven * dt
    venus.pos = venus.pos + venus.vel * dt

    aear = acc(earth)
    earth.vel = earth.vel + aear * dt
    earth.pos = earth.pos + earth.vel * dt

    amars = acc(mars)
    mars.vel = mars.vel + amars * dt
    mars.pos = mars.pos + mars.vel * dt

    t=t+dt