from body import Body
import random

class Dataset(object):
	def __init__(self):
		
		n=2
		fpos = 500000000
		fvel = 100
		
		self.bodies = []
		
		self.bodies.append(Body([-0.97000436, 0.24308753],
								[-0.93240737/2.0, -0.86473146/2.0],
								1.0,
								'#FF0000',
								'1'))
		
		self.bodies.append(Body([0.97000436, -0.24308753],
								[-0.93240737/2.0, -0.86473146/2.0],
								1.0,
								'#00FF00',
								'2'))
		
		self.bodies.append(Body([0.0, 0.0],
								[0.93240737, 0.86473146],
								1.0,
								'#0000FF',
								'3'))
		
		self.gravitationalConstant = 1
		self.minDist = 0
		self.skipFrames 		= 0
		self.timeStep 			= 0.01
		self.plotSize 			= 2.0
		self.annotationShift 	= self.plotSize/25.0
		self.markSizes 			= [50,200]
		self.lockedBody 		= -1