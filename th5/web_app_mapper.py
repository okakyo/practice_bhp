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

def test_remote():
    while not web_paths.empty():
        path=web_paths.get()
        url="{}{}".format(target,path)
        request=requests.get(url)

        try:
            response=requests.urlopen(request)
            content=response.read()

            print()
            response.close()

        except requests.HTTPError as err:
            pass

    for i in range(threads):
        print()
        t=threading.Thread()
        t.start()
