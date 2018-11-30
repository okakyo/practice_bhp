import Queue,threading,os,requests
threads=10

target='hpps://www.google.com'
directory='/Users/Kyohei Oka/Downloads/'
filters="['jpgs','gif','png','css']"

os.chdir(directory)
web_parser=Queue.Queue()

for r,d,f in os.walk("."):
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

        try:
            response=requests.get(url)
            print("[{}] => {}".format(response.status_code,path))
            response.close()

        except requests.HTTPError as err:
            print("Failed:{}".format(err.code))
            pass

    for i in range(threads):
        print()
        t=threading.Thread()
        t.start()
