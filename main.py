from threading import Thread
import requests
import os
from pathlib import Path
import re

def printArt():
    art = "	    __\n        ___/*_)\n       /= =\\/\n      /= = =\\                 ______\n     O --|-- O               |START |\n                             |______|\n                             |\n_____________________________|"
    print(art + '\n')
    print('___________________________________________________')
    print('---------------------------------------------------')
    print('###################### v=1.1 ######################')
    print('################### quickTurtle ###################')
    print('################ author: jajosheni ################')
    print('___________________________________________________')
    print('---------------------------------------------------')
    print('\n\n')

def getUri():
    while 1:
        uri = input('URL> ')

        if isdown(uri):
            return uri
        else:
            print("Cannot download this type of file")

def isEmpty(str):
    return not bool(str and str.strip())

def createfile():
    home = str(Path.home())

    global filename
    filename = input('\nfilename.extension> ')
    if isEmpty(filename):
        filename = "file.ext"

    try:
        if not os.path.isdir(home + "\\Desktop\\download"):
            os.system("mkdir " + home + "\\Desktop\\download")
        home += "\\Desktop\\download\\"

        while True:
            if os.path.exists(home + filename):
                print("File already exists.")
                cmd = input('Replace? (y/N)> ')

                if cmd.lower() != 'n':
                    break
                else:
                    filename = input('\nfilename.extension> ')
                    if isEmpty(filename):
                        filename = "file.ext"
            else:
                break
    except:
        pass

    if filename == "file.ext":
        print("Default name file.ext was choosen.\nChange the extension to open file.\n")

    filename = home + filename
    with open(filename, "wb") as myfile:
        myfile.close()

    return [home, filename]

def isdown(URL):
    try:
        h = requests.head(URL, allow_redirects=True)
        content_type = h.headers.get('content-type')

        if 'text' in content_type.lower() or 'html' in content_type.lower():
            return False
        else:
            return True
    except:
        return False

def get_length(URL):
    try:
        r = requests.head(URL)
        return r.headers['Content-Length']
    except Exception as e:
        print(e)

def downThread(i, URL, headers):
    print("started part{0} ".format(i))
    ranges = re.findall(r'\d+', headers['Range'])
    expectedsize = int(ranges[1]) - int(ranges[0])

    try:
        r = requests.get(URL, headers=headers, allow_redirects = True)
        try:
            partsize = len(r.content)
            if partsize == expectedsize + 1 or i == threadno:
                open(mypath[0] + "part{0}".format(i), 'wb').write(r.content)
            else:
                print("part{} didnt fully download, retrying...".format(i))
                downThread(i, URL, headers)
        except Exception as e:
            print(e)
    except Exception as e:
        print(e)

    print("finished part{0} ".format(i))

def downloadthis(URL, THREADS):
    threadslist=[]
    totallength=get_length(URL)
    avgLength=int(int(totallength)/int(THREADS))
    downrange=0

    for i in range(1 , THREADS+1 , 1):
        if i==THREADS:
            headers = {
                'Range': 'bytes=%s-%s' % (downrange, totallength) #last part
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
    for i in range(2):
        print("----------------------------------------------------")

    print("\nMerging files...")
    for i in range(1, THREADS+1 , 1):
        with open(filename, "ab") as myfile, open(str(mypath[0]) + "part{0}".format(i), "rb") as file2:
            myfile.write(file2.read())
            myfile.close()
            file2.close()
            os.remove(mypath[0] + "part{0}".format(i))


### RUN
while True:
    printArt()

    uri = getUri()
    mypath = createfile()

    try:
        threadno = int(input('\nhow many threads> '))
    except:
        print("choosing default... \n8 Threads.")
        threadno = 8



    threads = downloadthis(uri,int(threadno))

    for x in threads:
        x.join()

    merge(mypath[1], threadno)
    print("Download finished!")
    if str(input('Open Folder? (y/N) > ')).lower() == 'y':
        os.system("start {0}".format(mypath[0]))
    for i in range(2):
        print("----------------------------------------------------")
