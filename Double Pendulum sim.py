from visual import *
from visual.graph import *                              

## Physical constants.
mass1   = 1.0 # mass of pendulum bob 1
mass2   = mass1  #mass of pendulum bob 2
mtot    = mass1 + mass2  #total mass

length1 = .25*9.8 # length of pendulum 1
length2 = length1 #length of pendulum 2

grav    = 24.79
pi      = 3.14159265359


def secondDerivs(theta1, theta1dot, theta2, theta2dot, time):    ##defining the function and its independent variables


##Substitutions for Frequentyly Used Variables
    cos1    = cos(theta1)
    cos2    = cos(theta2)
    sin1    = sin(theta1)
    sin2    = sin(theta2)
    cos12   = cos(theta1-theta2)
    sin12   = sin(theta1-theta2)

    A       = mtot*length1
    B       = mass2*length2*cos12
    C       = -mtot*grav*sin1-mass2*length2*sin12*theta2dot**2
    D       = length2
    E       = length1*cos12
    F       = length1*sin12*theta1dot**2-grav*sin2

    

    

## Differential Equations

    theta1dotdot = (C-(B*F/D))/(A-(B*E/D))

    theta2dotdot = (F-E*theta1dotdot)/(D)

    energy = -mass1*grav*length1*cos1-mass2*grav*(length1*cos1+length2*cos2)+0.5*mass1*theta1dot**2*length1**2+0.5*mass2*(theta1dot**2*length1**2+theta2dot**2*length2**2+2*length1*length2*theta1dot*theta2dot*cos12)

    secondDerivs = [theta1dotdot, theta2dotdot, energy]  ##Stores Results. This is called a list. It will give us these values. He enters it on vid 4 at 19mins in

    
    return secondDerivs                      ##Tells python that thetadotdot is a function and to return values acording to variation in inputs


  



    

## Inital Conditions
time       = 0.0      #Start at t=0
tmax       = 400.0      #Maximum time to plot
dt         = 0.0005    #Small time increment (think Euler's method)


theta1     = 0.001*pi  #Starting angle (rad)
theta1dot  = 0.0           #Starting angle (rad/s)
theta2     = 0.001*pi
theta2dot  = 0.0

theta3     = 0.001*pi 
theta3dot  = 0.0
theta4     = 0.001*pi 
theta4dot  = 0.0


## Create visuals.
gdisplay(x=0,y=0,title = 'theta1 vs. time (white) & theta2 vs. time (green)')  #gdisplay refers to a graph. If you just have a visual (like the actual pendulum) just use display
theta1vstime = gcurve(color=color.white)     #defines the color of curve theta v time 
theta2vstime = gcurve(color=color.green)



gdisplay(x=0,y=0,title = 'Theta2 vs time (green) & theta 4 vs time (orange)')
theta2vstime = gcurve(color=color.green)
theta4vstime = gcurve(color=color.orange)



display(x=800,y=0)                          #This is the physical pendulum simulation
bob1 = sphere(pos=(length1*sin(theta1),-length1*cos(theta1),0),radius = length1/10.0,color=color.white)   ##this defines position of bob in (y,x)            radius = length/20.0)
rod1 = cylinder(pos=(0,0,0),axis=bob1.pos,radius=bob1.radius*0.1)                        
bob2 = sphere(pos=bob1.pos+(length2*sin(theta2),-length2*cos(theta2),0),radius = length2/10.0,color=color.green)
rod2 = cylinder(pos=bob1.pos,axis=bob2.pos-bob1.pos,radius=bob2.radius*0.1)



display(x=360,y=0)     ##second pendulum
bob3 = sphere(pos=(length1*sin(theta3),-length1*cos(theta3),0),radius = length1/10.0,color=color.white)   ##this defines position of bob in (y,x)            radius = length/20.0)
rod3 = cylinder(pos=(0,0,0),axis=bob3.pos,radius=bob3.radius*0.1)                        
bob4 = sphere(pos=bob1.pos+(length2*sin(theta4),-length2*cos(theta4),0),radius = length2/10.0,color=color.orange)
rod4 = cylinder(pos=bob3.pos,axis=bob4.pos-bob3.pos,radius=bob4.radius*0.1)

gdisplay(x=0,y=500,title = 'Energy vs. Time')
energyvstime = gcurve(color=color.green)

gdisplay(x=800,y=500,title = 'theta2 vs theta1')
theta2vstheta1 = gcurve(color=color.red)
theta4vstheta3 = gcurve(color=color.orange)




display(x=1238,y=0,title = 'parametric plot Pendulum 1')
##paraplotbob1 = sphere(make_trail=True,color=color.white,radius=length1/20.0)
paraplotbob2 = sphere(make_trail=True,color=color.green,radius=length1/30.0)
##paraplotbob3 = sphere(make_trail=True, color=color.red,radius=length1/20.0)
paraplotbob4 = sphere(make_trail=True,color=color.orange,radius=length1/30.0)






while time < tmax:
    rate(10000)
    time      = time + dt
    thetadotdot = secondDerivs(theta1, theta1dot, theta2, theta2dot, time) ##thetadotdot is making a list and the following functions call off of that list         

    theta1dot = theta1dot + thetadotdot[0]*dt  ##calls theta1dotdot 
    theta1    = theta1 + theta1dot*dt
    theta2dot = theta2dot + thetadotdot[1]*dt  ##calls theta2dotdot 
    theta2    = theta2 + theta2dot*dt              
    
    bob1.pos  = (length1*sin(theta1),-length1*cos(theta1),0)
    rod1.pos  = (0,0,0)
    rod1.axis = bob1.pos
    bob2.pos  = bob1.pos+(length2*sin(theta2),-length2*cos(theta2),0)
    rod2.pos  = bob1.pos
    rod2.axis = bob2.pos - bob1.pos

  
   

    thetadotdot = secondDerivs(theta3, theta3dot, theta4, theta4dot, time)

    theta3dot = theta3dot + thetadotdot[0]*dt
    theta3    = theta3 + theta3dot*dt
    theta4dot = theta4dot + thetadotdot[1]*dt
    theta4    = theta4 + theta4dot*dt
    
    bob3.pos  = (length1*sin(theta3),-length1*cos(theta3),0)
    rod3.pos  = (0,0,0)
    rod3.axis = bob3.pos
    bob4.pos  = bob3.pos+(length2*sin(theta4),-length2*cos(theta4),0)
    rod4.pos  = bob3.pos
    rod4.axis = bob4.pos - bob3.pos


    theta2vstime.plot(pos=(time,theta2))
    theta4vstime.plot(pos=(time,theta4))
##        
    theta1vstime.plot(pos=(time,theta1))
    theta2vstime.plot(pos=(time,theta2))
##
##
    theta2vstheta1.plot(pos=(theta1,theta2))
    theta4vstheta3.plot(pos=(theta3,theta4))

    
    
    
    energyvstime.plot(pos=(time,thetadotdot[2]))

  ##  paraplotbob1.pos = (bob1.pos) inside bobds get confusing on grapb
    paraplotbob2.pos = (bob2.pos)
 ##   paraplotbob3.pos = (bob3.pos)
    paraplotbob4.pos = (bob4.pos)

    
 
 ##   uvstheta.plot(pos=(theta,mass*grav*length-mass*grav*length*cos(theta)))
 ##   kvstheta.plot(pos=(theta,0.5*mass*math.pow(length*thetadot*cos(theta),2)+0.5*mass*math.pow(length*thetadot*sin(theta),2)))
 









     

    
