from body import Body
import random

class Dataset(object):
	def __init__(self):
	
		n=2
		fpos = 500000000
		fvel = 100
	
		self.bodies = []
		
		self.bodies.append(Body([0.0, 0.0],
								[0.0, 0.0],
								1.0*(10**23),
								'#000000',
								'Center'))
		
		for i in range(n):
			x = 1.0/n*i
			self.bodies.append(Body([fpos*x+fpos/2.0, 0.0],
									[0.0, 2*fvel*(1-x)],
									1.0*(10**21),
									'#5566ff',
									str(i+1)))

		self.skipFrames 		= 0
		self.timeStep 			= 10000
		self.plotSize 			= 1000000000
		self.annotationShift 	= self.plotSize/25.0
		self.markSizes 			= [50,400]
		self.lockedBody 		= -1