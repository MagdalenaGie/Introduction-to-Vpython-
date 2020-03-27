from vpython import *
import numpy as np

scene=canvas(width=800, height=800)
sun=sphere(canvas=scene, pos=vec(-150*10**9, 0, 0), radius=10**10, vel=-vec(0, 30*10**3, 0), color=color.yellow, make_trail=True)
mercury=sphere(canvas=scene, pos=vec(70*10**9, 0, 0)+sun.pos, radius=6*10**9, color=color.white, vel=vec(0, 47*10**3, 0), make_trail=True)
venus=sphere(canvas=scene, pos=vec(110*10**9, 0, 0)+sun.pos, radius=6*10**9, color=color.green, vel=vec(0, 35*10**3, 0), make_trail=True)
earth=sphere(canvas=scene, pos=vec(0, 0, 0), radius=6*10**9, color=color.blue, vel=vec(0, 30*10**3, 0), make_trail=True)
mars=sphere(canvas=scene, pos=vec(250*10**9, 0, 0)+sun.pos, radius=6*10**9, color=color.red, vel=vec(0, 24*10**3, 0), make_trail=True)

def accs(planet):
    G = 6.7 * 10 ** (-11)
    Ms=2*10**30
    r=mag(planet.pos)
    a=-G*Ms/(r**3)*(planet.pos)
    return a

def acc(planet):
    G = 6.7 * 10 ** (-11)
    Ms=2*10**30
    r=mag(planet.pos-sun.pos)
    a=-G*Ms/(r**3)*(planet.pos-sun.pos)
    return a


t=0
dt=3600
while t<5*31536000:
    rate(2000)
    amerc = acc(mercury)
    mercury.vel = mercury.vel + amerc * dt
    mercury.pos = mercury.pos + mercury.vel * dt + sun.vel * dt

    asun = accs(sun)
    sun.vel = sun.vel + asun * dt
    sun.pos = sun.pos + sun.vel * dt

    aven = acc(venus)
    venus.vel = venus.vel + aven * dt
    venus.pos = venus.pos + venus.vel * dt + sun.vel * dt

    amars = acc(mars)
    mars.vel = mars.vel + amars * dt
    mars.pos = mars.pos + mars.vel * dt + sun.vel * dt

    t=t+dt
