import socet,sys,getopt,threading,subprocess

listen=False
command=False
upload=""
target=""
upload_destination=""
port=0

def useage():
    print("BHP Net Tool")
    print()
    print("Useage:netcat.py -t target_host -p port")
    print("-l listen                 -listen on [host]:[port] for")
    print("                          incoming connections")
    print("-e --excute=file_to run   -execute the given file upon"  )
    print("                           recieving a connection")
    print("-c --command              -initialize a command shell ")
    print("-u --upload=destination   -upon recieving connection upload a")
    print("                           file and write to [destination]")
    print()
    print()
    print("Examples:")
    print("netcat.py -t 192.168.0.1 -p 5555 -l -c")
    print("netcat.py -t 192.168.0.1 -p 5555 -l -u c://target.exe")
    print("netcat.py -t 192.168.0.1 -p 5555 -l -e \"cat /etc/passwd\"")
    print('echo "ABCDEFGH"| ./netcat.py -t 192.168.11.12 -p 135 ')
    sys.exit(0)

def main():
    global listen,port,execute,command,upload_destination,target
    if not len(sys.argv[1:]):
        useage()
    try:
        opts,args=getopt.getopt(
                sys.argv[1:],
                "hle:t:p:cu",
                ["help","listen","execute=","target=","port=","command","upload="]
                )
    except get.GetoptError as err:
        print(str(err))
        useage()

    for o,a in opts:
        if o in ("-h" or "--help"):
            useage()
        elif o in ("-h" or "--help"):
            listen=True
        elif o in ("-h" or "--help"):
            execute=a
        elif o in ("-h" or "--help"):
            command=True
        elif o in ("-h" or "--help"):
            upload_destination=a
        elif o in ("-h" or "--help"):
            target=a
        elif o in ("-h" or "--help"):
            port=int(a)
        else:
            assert (False, "Unhandled Option")
    if not listen and len(target) and port>0:
        buffer=sys.stdin.read()
        client_sender(buffer)

    if listen:
        server_loop()

def client_sender():
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        client.connect((target,port))
        if len(buffer):
            client.send(buffer)
        while True:
            recv_len=1
            response=""
            while recv_len:
                data=client.recv(4096)
                recv_len=len(data)
                response+=data
                if recv_len<4096:
                    break
            print(response)

            buffer=input("")
            buffer+="\n"
            client.send(buffer)
    except:
        print("[*] Exception! Exiting.")
        client.close()

def server_loop():
    global target

    if not len(target):
        target="0.0.0.0"

    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((target,port))
    server.listen(5)
    while True:
        client_thread=threading.Thread(
                target=client_handler,args=(client_socket,))
        client_thread.start()

def run_command(command):
    command=command.rstrip()
    try:
        output=subprocess.check_output(
                command.stderr=subprocess.STDOUT,shell=True)
    except:
        output="Failed to execute command.\r\n"
    return output

def client_handler(clienct_socket):
    global upload,execute,command
    if len(upload_destination):
        file_buffer=""
        while True:
            data=client_socket.recv(1024)
            if len(data)==0:
                break
            else:
                file_buffer+=data
        try:
            with open(upload_destination,"wb") as w:
                w.write(file_buffer)
            client_socket.send(
                    "Successfully saved file  to {}\r\n".format(upload_destination))
        except:
            client_socket.send(
                    "Failed to save file to {}\r\n".format(upload_destination))
    if len(execute):
        output=run_command(execute)
        client_socket.send(output)
    if command:
        prompt="<BHP:#>"
        client_socket.send(prompt)
        while True:
            cmd_buffer=""
            while "\n" not in cmd_buffer:
                cmd_buffer+=client_socket.recv(1024)
            response+=run_command(cmd_buffer)
            respomse+=prompt
            client_socket,send(response)


if __name__=='__main__':
    main()
