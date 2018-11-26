import threading,paramiko,subprocess

#以下のコマンドは、BASIC認証での場合で実証する場合に使う。

def ssh_command(ip,user,passwd,command):
    client=paramiko.SSHClient()

    #client.load_host_keys('/home/name/.ssh/known_hosts')
    #上記の方法でSSH接続する。
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip,username=user,password=passwd)
    ssh_session=client.get_tansport().open_session()
    if ssh_session.active:
        ssh_session.exec_command(command)
        print(ssh_session.recv(1024))
    return

ssh_command('192.168.223.136','name','password','id')
