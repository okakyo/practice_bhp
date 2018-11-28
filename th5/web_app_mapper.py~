import Queue,threading,os,requests
threads=10

target='hpps://www.google.com'
directory='/Users/Kyohei Oka/Downloads/'
filters="['jpgs','gif','png','css']"

os.chdir(directory)
web_parser=Queue.Queue()

for r,d,f in os.walk():
    for files in f:
        remote_path='{}/{}'.format(r,files)
        if remote_path.startswith('.'):
            remote_path=remote_path[1:]
        if os.path.splittext(files)[1] not in filters:
            web_paths.put(remote_path)

