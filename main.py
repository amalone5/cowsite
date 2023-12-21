from flask import Flask, render_template
from randomcow import *


#buildwebsite2()
# TODO: make button work
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

localcowcount=0

@app.route('/my-link/')
def my_link():
    global localcowcount
    print ('I got clicked!')
    buildwebsite2()
    sitename="cow"+str(localcowcount)+".html"
    localcowcount = localcowcount+1
    print("rendering "+sitename)
    return render_template(sitename)

if __name__ == '__main__':
    app.run(debug=True)
 
