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
main()



