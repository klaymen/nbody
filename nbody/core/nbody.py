class Nbody(object):
    # Prepare and run an N-body simulation

    def __init__(self, bodies):
        # Create a new simulation
        # bodies - list of bodies to be considered in the simulation

        self.G          = 6.67384*(10**(-11))   # Gravitational constant 
                                                # [m3 kg-1 s-2]
        self.minDist    = 10**1                 # Distance within there are no 
                                                # forces applied (preventing 
                                                # large accelerations)[m]
        self.bodies     = bodies                # Participating bodies
        self.dimension  = min([body.getDimension() for body in bodies]) # Dimension of simulation
        self.elapsedTime = 0                    # Reset time

    def calcAcc(self, body1, body2):
        # Calculate the acceleration on body1 from body2
        # body1 - body being accelerated
        # body2 - body that exerts it's gravitational pull on the other

        # Fx = (G * mass1 * mass2)(x2 - x1)/(distance^3)
        distance = body1.getDistance(body2)
        total_force =  self.G * body1.mass * body2.mass
        total_force /= distance**2
        
        force = [0.0] * self.dimension
        acc   = [0.0] * self.dimension
        
        for d in range(self.dimension):
        
            # Force in the dth dimension (considering the direction as well)
            force[d] = (body2.pos[d] - body1.pos[d])*total_force/distance
        
            # Prevent unreasonably large accelerations 
            # by limiting the minimum distance.
            if -self.minDist < body2.pos[d] - body1.pos[d] < self.minDist:
                force[d] = 0.0
          
            # Acceleration = Force/mass
            acc[d] = force[d]/body1.mass
            
        return acc

    def step(self, dt):
        # Perform one time step of the simulation
        # dt - time step [s]

        # Calculate the new acceleration for each body by iterating through each
        # body and calculating the force excreted by it
        for body1 in self.bodies:

            # Reset accelerations for the new step
            body1.acl = [0.0] * self.dimension

            for body2 in self.bodies:
                if body2 != body1:
                    acl = self.calcAcc(body1, body2)

                    # Update accelerations
                    for d in range(self.dimension):
                        body1.acl[d] += acl[d]

        # Update velocities and positions (Forward Euler)
        for body in self.bodies:
            for d in range(self.dimension):
                body.vel[d] += body.acl[d] * dt
                body.pos[d] += body.vel[d] * dt

        self.elapsedTime += dt # Update elapsed time
        
    def getCoords(self):
        #Return coordinates of the corresponding bodies
        
        results = [[] for d in range(self.dimension)]
        
        for body in self.bodies:
            for d in range(self.dimension):
                results[d].append(body.pos[d])
                
        return results

    def getMasses(self):
        return [i.mass for i in self.bodies]
        
    def getColors(self):
        return [i.colr for i in self.bodies]
