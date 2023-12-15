import random
import os
import sys

pathtodir=""
cowpath=""
index=""

def setPaths():
    if(len(sys.argv) <= 1):
        print("wrong args, exiting")
        quit()
    global pathtodir
    global cowpath
    global index
    pathtodir=sys.argv[1]
    cowpath=pathtodir+"/cows.txt"
    index=pathtodir+"/index.html"

def printpaths():
    print("pathtodir: "+pathtodir)
    print("cowpath: "+cowpath)
    print("index: "+index)

def getCows():
    cowfile = open(cowpath,"r")
    cows = []
    for cow in cowfile:
        cows.append(cow.strip())
    return cows

def getRandomCow():
    return random.choice(getCows())

def buildtop():
    os.system("echo '<!DOCTYPE html>' > "+index)
    os.system("echo '<html lang=\"en\">' >> "+index)
    os.system("echo '<head>' >> "+index)
    os.system("echo '    <meta charset=\"UTF-8\">' >> "+index)
    os.system("echo '    <title>Fortune</title>' >> "+index)
    os.system("echo '</head>' >> "+index)
    os.system("echo '<body>' >> "+index)

def sendRandomCowToFile():
    os.system("echo '<pre>' >> "+index)
    os.system("fortune | cowsay -f "+getRandomCow()+" >> "+index)
    os.system("echo '</pre>' >> "+index)

def buildbottom():
    os.system("echo '</body>' >> "+index)
    os.system("echo '</html>' >> "+index)

def helloworld():
    print("helloworld!")
