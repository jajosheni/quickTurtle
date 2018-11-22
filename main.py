from threading import Thread
import requests
import os
from pathlib import Path

def get_length(URL):
    r = requests.head(URL)
    return(r.headers['Content-Length'])

def downThread(i, URL, headers):
    print("started part{0} ".format(i))
    r = requests.get(URL, headers=headers)
    open(home + "part{0}".format(i), 'wb').write(r.content)
    print("finished part{0} ".format(i))


def downloadthis(URL, THREADS):
    threadslist=[]
    totallength=get_length(URL)
    avgLength=int(int(totallength)/int(THREADS))
    downrange=0

    for i in range(1 , THREADS+1 , 1):
        if i==THREADS:
            headers = {
                'Range': 'bytes=%s-%s' % (downrange, totallength)
            }
        else:
            headers = {
                'Range': 'bytes=%s-%s' % (downrange, downrange+avgLength)
            }
        downrange+=avgLength+1

        t = Thread(target=downThread, args=(i,URL,headers,))
        threadslist += [t]
        t.start()
    return threadslist


def merge(filename, THREADS):
    os.system("cls")
    print("Merging files...")
    for i in range(1, THREADS+1 , 1):
        with open(filename, "ab") as myfile, open(home + "part{0}".format(i), "rb") as file2:
            myfile.write(file2.read())
            myfile.close()
            file2.close()
            os.remove(home + "part{0}".format(i))


### RUN
uri = input('quickTurtle> URL:')

filename = input('quickTurtle> filename.extension: ')
home = str(Path.home())
try:
    os.system("mkdir " + home + "\\Desktop\\download")
    home +="\\Desktop\\download\\"
except:
    pass
filename = home + filename

threadno = int(input('quickTurtle> how many threads: '))

with open(filename, "wb") as myfile:
    myfile.close()

threads = downloadthis(uri,threadno)

for x in threads:
    x.join()

merge(filename, threadno)
print("Download finished!")
os.system("start {0}".format(home))
