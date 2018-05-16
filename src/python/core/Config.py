import os
from os.path import expanduser

class Config(object):
	"""Runner configurations"""
# 	def __init__(self):
# 		defects4jRepairRoot = os.path.join(os.path.dirname(__file__),'../../../' )
# 
# 		self.defects4jRepairRoot = defects4jRepairRoot
# 		self.projectsRoot = expanduser("/mnt/secondary/projects")
# 		self.defects4jRoot = expanduser("~/git/defects4j")
# 		self.resultsRoot = os.path.join(defects4jRepairRoot, "results/2016-november")
# 		self.z3Root = os.path.join(defects4jRepairRoot, "libs", "z3")
# 		self.javaHome = expanduser("/usr/lib/jvm/java-7-openjdk-amd64/bin/")
# 		self.javaHome8 = expanduser("/usr/lib/jvm/jdk1.8.0_73/bin/")
# 		self.javaArgs = "-Xmx4096m"

	def __init__(self):		
		defects4jRepairRoot = os.path.join(os.path.dirname(__file__),'../../../' )
		self.defects4jRepairRoot = defects4jRepairRoot
		self.projectsRoot = expanduser("~/projects")
		self.defects4jRoot = expanduser("~/defects4j")
		self.resultsRoot = os.path.join(defects4jRepairRoot, "results/2018-april")
		self.z3Root = os.path.join(defects4jRepairRoot, "libs", "z3")
		self.javaHome = expanduser("/usr/lib/jvm/java-7-oracle/bin/")
		self.javaHome8 = expanduser("/usr/lib/jvm/java-8-oracle/bin/")
		
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
		
conf = Config()
