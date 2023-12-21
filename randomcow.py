import random
import os
import sys

pathtodir=""
cowpath="./cows.txt"
index="./templates/index.html"

def setPaths():
    if(len(sys.argv) <= 1):
        print("wrong args, exiting")
        quit()
    global pathtodir
    global cowpath
    global index
    pathtodir=sys.argv[1]
    cowpath=pathtodir+"/cows.txt"
    index=pathtodir+"/templates/index.html"

def showargs():
    i=0
    for arg in sys.argv:
        print("arg"+str(i)+": "+arg)
        i=i+1

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
    os.system("echo '<!DOCTYPE html>' >> "+index)
    os.system("echo '<html lang=\"en\">' >> "+index)
    os.system("echo '<head>' >> "+index)
    os.system("echo '    <meta charset=\"UTF-8\">' >> "+index)
    os.system("echo '    <title>cowsite</title>' >> "+index)
    os.system("echo '</head>' >> "+index)
    os.system("echo '<body>' >> "+index)

def buildtop(index):
    os.system("echo '<!DOCTYPE html>' >> "+index)
    os.system("echo '<html lang=\"en\">' >> "+index)
    os.system("echo '<head>' >> "+index)
    os.system("echo '    <meta charset=\"UTF-8\">' >> "+index)
    os.system("echo '    <title>cowsite</title>' >> "+index)
    os.system("echo '</head>' >> "+index)
    os.system("echo '<body>' >> "+index)


def sendRandomCowToFile():
    os.system("echo '<pre>' >> "+index)
    os.system("fortune | cowsay -f "+getRandomCow()+" >> "+index)
    os.system("echo '</pre>' >> "+index)

def sendRandomCowToFile(index):
    os.system("echo '<pre>' >> "+index)
    os.system("fortune | cowsay -f "+getRandomCow()+" >> "+index)
    os.system("echo '</pre>' >> "+index)

def buildbottom():
    os.system("echo '</body>' >> "+index)
    os.system("echo '</html>' >> "+index)

def buildbottom(index):
    os.system("echo '</body>' >> "+index)
    os.system("echo '</html>' >> "+index)

def buildbutton():
    button_html="<button> <a href=\"/my-link/\">Click me</a></button>"
    # os.system("echo '<button type\"button\">Click Me!</button>' >> "+index)
    os.system("echo '"+button_html+"' >> "+index)

def buildbutton(index):
    button_html="<button> <a href=\"/my-link/\">Click me</a></button>"
    # os.system("echo '<button type\"button\">Click Me!</button>' >> "+index)
    os.system("echo '"+button_html+"' >> "+index)

def clearindex():
    os.system("echo '' > "+index)

def removeindex(index):
    os.system("rm "+index)

def helloworld():
    print("helloworld!")

def buildwebsite():
    # setPaths()
    clearindex()
    buildtop()
    sendRandomCowToFile()
    buildbutton()
    buildbottom()


cowcount=0

def buildwebsite2():
    global cowcount
    # os.system('rm ./templates/cow'+str(cowcount)+".html")
    cowpath = "./templates/cow"+str(cowcount)+".html"
    cowcount = cowcount+1
    buildtop(cowpath)
    sendRandomCowToFile(cowpath)
    buildbutton(cowpath)
    buildbottom(cowpath)

