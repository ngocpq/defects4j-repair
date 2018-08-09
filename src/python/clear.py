import os
import subprocess

cmd = 'ps -u ngocpq'
res = subprocess.check_output(cmd, shell=True)
#print(cmd)

ignoreList = ['bash', 'systemd', '(sd-pam)', 'sshd', 'htop', 'ps', 'sh', 'python']
killList = ['defects4j', 'astor','java']

ExceptionList = []

print('--------- killing processes: ------')

lines = res.split('\n')[1:]
for line in lines:
    if len(line) == 0:
        continue
    #print(line)
    ExceptionList = line.split()
    if len(ExceptionList) == 5:
	pid, tty, time, cmd, cmd0 = line.split()
    else:
    	pid, tty, time, cmd = line.split()
    	if cmd in ignoreList:
        	continue
	if cmd in killList:        	
	    #print(pid, tty, time, cmd)
	    cmd = 'kill -9 {}'.format(pid)
	    print(cmd)
	    os.system(cmd)

#os.system('pkill -9 -ef defects4j')
os.system('pkill -9 -ef java')
#os.system('pkill -9 -ef python')

