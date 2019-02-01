
class ParaSetting(object):
	"""Runner configurations"""
	def __init__(self):		
		#setting the RAM memory size
		#self.javaArgs = "-Xmx4096m"
		#self.javaArgs = "-Xmx768m"
		self.javaArgs = "-Xmx512m"
		
		#setting the repair parameters
		self.flthreshold = 0.1
		self.scope = "package"
		self.seed = 300
		self.population = 20
		self.maxgen = 500
		self.stopfirst = True
		self.maxtime = 180
		self.loglevel = "INFO"
		self.saveall = True
		self.parameters = "logtestexecution:true:runexternalvalidator:true"
		
para = ParaSetting()
