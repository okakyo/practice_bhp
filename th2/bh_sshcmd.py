import threading,paramiko,subprocess

#�ȉ��̃R�}���h�́ABASIC�F�؂ł̏ꍇ�Ŏ��؂���ꍇ�Ɏg���B

def ssh_command(ip,user,passwd,command):
    client=paramiko.SSHClient()

    #client.load_host_keys('/home/name/.ssh/known_hosts')
    #��L�̕��@��SSH�ڑ�����B
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip,username=user,password=passwd)
    ssh_session=client.get_tansport().open_session()
    if ssh_session.active:
        ssh_session.exec_command(command)
        print(ssh_session.recv(1024))
    return

ssh_command('192.168.223.136','name','password','id')
