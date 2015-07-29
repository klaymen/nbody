from body import Body

class Dataset(object):
	def __init__(self):
		self.bodies = []
		
		self.bodies.append( Body(	[384400000, 0.0],	# position [m]
									[0.0, 1000.0],		# velocity [m s-1]
									7.347*(10**22),		# mass [kg]
									'#999999',			# color
									'Moon'))			# name
		
		self.bodies.append( Body(	[0.0, 0.0],
									[0.0, 0.0],
									5.97*(10**24),
									'#009900',
									'Earth'))

		self.skipFrames 		= 0
		self.timeStep 			= 1000
		self.plotSize 			= 1000000000
		self.annotationShift 	= self.plotSize/25.0
		self.markSizes 			= [50,400]
		self.lockedBody 		= -1
		self.dataTodisplay		= "TotalImpulse"