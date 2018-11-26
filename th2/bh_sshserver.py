import threading.paramiko,socket,sys

host_keys=paramiko.RSAKey(filenames='test_rsa.key')

class Server(paramiko.ServerInterface):
    def __init__(self):
        self.event=threading.Event()
    
    def check_channel_request(self,kind,chanid):
        if kind=='session':

            return paramiko.OPEN_SUCCESSED

        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

    def check_auth_password(self,username,password):
        if (username=='name') and (password=='password'):
            return paramoko.AUTH_SUCCESSFUL
        return paramiko.AUTH_FAILED

server=sys.argv[1]

ssh_port=int(sys.argv[2])

try:
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    sock.bind((server,ssh_port))
    sock.listen(100)
    print("[+] Linstening for connection...")
    client,addr=sock.accept()
except Exception as e:
    print("[-] Listen failed: "+str(e))
    sys.exit(1)
print("[+] Got a connection !")

try:
    bhSsesion=paramiko.Transport(client)
    bhSession.add_server_key(host_key)
    server=Server()
    try:
        bhSession.start_server(server=server)
    except paramiko.SSHException as x:
        print("[-] SSH negotiation failed.")
    
    chain=bhSession.accept(20)
    print("[+] Authenticated !")
    print(chain.recv(1024))
    chain.send('Welcome to bh_ssh')
    while True:
        try:
            command=input("Enter command: ").strip('\n')
            if command!='exit':
                chain.send(command)
                print(chain.recv(1024)+'\n')
            else:
                chain.send('exit')
                print('Exiting')
                bhSession.close()
                raise( Exception ('exit'))
        except KeyboardInterrupt:
            bhSession.close()
except Exception as e:
    print('[-] Caught exception: '+str(e))
    try:
        bhSession.close()
    except:
        pass
    sys.exit(1)

