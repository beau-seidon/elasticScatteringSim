# elastic collision simulator

from time import time as t
import matplotlib.pyplot as plt


# initial parameters
m1 = 0.02     # mass [kg]
iVel1 = 10   # initial velocity [m/s]
fVel1 = 0   # final velocity (unknown) [m/s]
iPos1 = 0   # initial position [m]
rad1 = 0.005    #radius [m]

m2 = 0.005  # mass [kg]
iVel2 = -5  # initial velocity [m/s]
fVel2 = 0   # final velocity (unknown) [m/s]
iPos2 = 10  # initial position [m]
rad2 = 0.005    #radius [m]


# indicies
mass = 0
position = 1
initVelocity = 2
finVelocity = 3


# particle = [mass, position, initVelocity, finVelocity]
particle1 = [m1, iPos1, iVel1, fVel1]
particle2 = [m2, iPos2, iVel2, fVel2]


def collide(p1, p2):
    p1[finVelocity] = ((p1[mass] - p2[mass]) * p1[initVelocity] + 2 * p2[mass] * p2[initVelocity]) / (p1[mass] + p2[mass])
    p2[finVelocity] = ((p2[mass] - p1[mass]) * p2[initVelocity] + 2 * p1[mass] * p1[initVelocity]) / (p1[mass] + p2[mass])

    print('particle 1 initial momentum = ' + str(p1[mass] * p1[initVelocity]) + ' [kg*m/s]')
    print('particle 1 final momentum = ' + str(p1[mass] * p1[finVelocity]) + ' [kg*m/s]')
    print('particle 2 initial momentum = ' + str(p2[mass] * p2[initVelocity]) + ' [kg*m/s]')    
    print('particle 2 final momentum = ' + str(p2[mass] * p2[finVelocity]) + ' [kg*m/s]')


# main
t0 = t()
dt = 0

tLog = [0]
pLog1 = [particle1[position]]
pLog2 = [particle2[position]]

collid = False

separation = particle2[position] - particle1[position]
initSep = separation

while (abs(separation) <= initSep):
    if (t() > t0):
        dt = t() - t0
        t0 = t()

        if not collid and (abs(separation) <= (rad1 + rad2)):
            collid = True
            collide(particle1, particle2)

        particle1[position] = particle1[position] + ((particle1[initVelocity] * (not collid)) + (particle1[finVelocity] * collid)) * dt
        particle2[position] = particle2[position] + ((particle2[initVelocity] * (not collid)) + (particle2[finVelocity] * collid)) * dt

        separation = particle2[position] - particle1[position]

        tLog.append(tLog[-1] + dt)
        pLog1.append(particle1[position])
        pLog2.append(particle2[position])

plt.plot(pLog1, tLog)
plt.plot(pLog2, tLog)
#plt.legend()
plt.show()




###   particle object constructor (incomplete and unused)
##class particle:
##	def __init__(self, mass, position):
##		self.mass = mass
##		self.position = position
##		
##	prevPos = self.position
##	prevTime = time
##	
##	def velocity(self, prevPos, prevTime):
##		x0 = self.prevPos
##		x = self.position
##		t0 = self.prevTime
##		t = time()
##		
##		self.velocity = (x - x0) / (t - t0 )
##		
##		self.incrementTime(prevTime)
##		
##	def
##		
##	def incrementTime(self):
##		self.prevTime = t()
