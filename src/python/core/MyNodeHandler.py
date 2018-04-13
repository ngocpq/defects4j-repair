import os
import re
import sys
import math
import time
import json
import datetime
import subprocess

class MyNodeHandler(object):
	"""docstring for NodeHandler"""
	def __init__(self, tasks):
		self.maxNode = 50
		self.tasks = tasks
		self.running = 0
		self.init = False
		
	def run(self, timeoutNode=None):
		totalTask = len(self.tasks)
		self.toExecuteTask = []
		self.toExecuteTask += self.tasks
		startTime = time.time()
		self.taskOARId = {}
		print "Execute %d tasks" % totalTask
		while(len(self.toExecuteTask) > 0):
			task = self.toExecuteTask.pop()
			filename = task.project.name.lower() + '_' + str(task.id)
			stdoutlog =  os.path.join(task.project.logPath, str(task.id), task.tool.name, 'stdout.log')
			stderrlog =  os.path.join(task.project.logPath, str(task.id), task.tool.name, 'stderr.log')
			resultlog =  os.path.join(task.project.logPath, str(task.id), task.tool.name, 'results.json')

			if not os.path.exists(os.path.dirname(stdoutlog)):
				os.makedirs(os.path.dirname(stdoutlog))

			if not os.path.exists(os.path.dirname(stderrlog)):
				os.makedirs(os.path.dirname(stderrlog))

			cmd = 'rm %s; ' % stdoutlog
			cmd += 'rm %s; ' % stderrlog
			cmd += 'rm %s; ' % resultlog

			nodeCmdArgs = "%s -p %s -t %s -i %d" % (
				os.path.join(os.path.dirname(__file__), '..', 'defects4j-g5k-node.py'),
				task.project.name,
				task.tool.name,
				task.id
			)
			nodeCmd = "python %s" % nodeCmdArgs 
			

			# cmd += path
			cmd += "oarsub -l nodes=1,walltime=%s -O %s -E %s \"%s\"" % (
				timeoutNode if timeoutNode else task.tool.maxExecution,
				stdoutlog,
				stderrlog,
				nodeCmd
			)
			devnull = open('/dev/null', 'w')
			#cmdOutput = subprocess.check_output(nodeCmd, shell=True, stdin=None, stderr=devnull)
			print "nodecmd: " + nodeCmd
			cmdOutput = subprocess.check_output(nodeCmd, shell=True, stdin=None, stderr=devnull)			
			
			print "output: %s" % cmdOutput
# 			m = re.search('OAR_JOB_ID=([0-9]+)', cmdOutput)
# 			if m:
# 				jobId = int(m.group(1))
# 				self.taskOARId[task] = jobId
# 				self.running += 1
# 				self.printStatus(totalTask, startTime)
			
		print "Execute %d tasks in %2.2f sec" % (totalTask, time.time() - startTime)
		
	def printStatus(self, totalTask, startTime):
		output = "%d tasks to run, %d tasks running, %d completed (%2.2f%%), running for %s\n" % (
			len(self.toExecuteTask),
			self.running,
			(totalTask-len(self.toExecuteTask)-self.running),
			(totalTask-len(self.toExecuteTask)-self.running)/float(totalTask)*100,
			datetime.timedelta(seconds=int(time.time() - startTime)))
		output += "      |";
		bugs = {}
		tools = []
		for task in self.tasks:
			key = "%s%d" % (task.project.name[0], task.id)
			if key not in bugs:
				bugs[key] = {}
			bugs[key][task.tool.name] = task
			if task.tool.name not in tools:
				tools += [task.tool.name]
		tools.sort()
		for tool in tools:
			output += " {0:8} |".format(tool)
		output += "\n------|"
		for tool in tools:
			output += "----------|"
		output += "\n"
		states = self.getRunning()
		odd = True

		for (bugId, bug) in sorted(bugs.iteritems(), key=lambda (k,v): natural_keys(k)):
			if odd:
				#sys.stdout.write("\033[37m")
				output += "\x1b[7;37;40m"
			else:
				#sys.stdout.write("\033[30m")
				output += ("\x1b[7;30;47m")
			odd = not odd
			output += " {0:4} |".format(bugId)
			for tool in tools:
				if tool in bug:
					task = bug[tool]
					if task in self.toExecuteTask:
						output += " {0:8} |".format("Queue")
					elif str(self.taskOARId[task]) in states:
						state = states[str(self.taskOARId[task])]
						if state['state'] == "Running":
							output += " {0:8} |".format(datetime.timedelta(seconds=int(time.time() - float(state['startTime']))))
						else:
							output += " {0:8} |".format(state['state'])
					else:
						resultlog =  os.path.join(task.project.logPath, str(task.id), task.tool.name, 'results.json')
						stderrToolPath =  os.path.join(task.project.logPath, str(task.id), task.tool.name, 'stderr.log')
						if os.path.exists(resultlog):
							with open(resultlog) as data_file:
								results = json.load(data_file)
								if (("patch" in results and results["patch"]) or
									("operations" in results and len(results["operations"]) > 0)):
									output += " {0:8} |".format("Fixed")
								else:
									output += " {0:8} |".format("No")
						elif os.path.exists(stderrToolPath):
							with open(stderrToolPath) as data_file:
								data = data_file.read()
								m = re.search("Job [0-9]+ KILLED", data)
								if m:
									output += " {0:8} |".format("Timeout")
								elif len(data) == 0:
									output += " {0:8} |".format("Empty")
								else:
									output += " {0:8} |".format("Error")
			output += "\x1b[0m\n"		
		self.init = True
		print output
		
	
def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split('(\d+)', text) ]
