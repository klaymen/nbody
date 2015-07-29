from math import sqrt

class Body(object):
    # A very simple class to store some basic properties
    # of a celestial body

    def __init__(self, pos, vel, mass, colr = "#999999", name = "Unknown"):
        # pos - components of the body's position [m]
        # vel - components of the body's velocity [m s-1]
        # mass - Mass of the body [kg]
        # colr - Display color of the body
        # name - Name of the celestial body
        
        self.pos  = pos
        self.vel  = vel
        self.mass = mass
        self.colr = colr
        self.name = name
        
        self.acl  = [0.0] * len(self.pos)  # Acceleration vector [m s-2]

    def getDistance(self, body):
        # Compute the distance from an other body
        # TODO: should be n dimensional
        return  sqrt((self.pos[0]-body.pos[0])**2 + (self.pos[1]-body.pos[1])**2)

    def getDimension(self):
        return min(len(self.pos), len(self.vel))

    def getSpeed(self):
        return [c for c in self.vel]
