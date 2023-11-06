from lib.microdot import Microdot, Response, redirect
from lib.microdot_utemplate import render_template
import utime, _thread

from machine import Pin
# from lib.chatbot import chat

onboard = Pin("LED", Pin.OUT)

# global variables
ledState = False
reply = ""

app = Microdot()
Response.default_content_type = 'text/html'

@app.route('/')
def index(request):
    return render_template('login.html')


@app.route('/login', methods=["POST"])
def login(request):
    uname = request.form.get('uname')
    pword = request.form.get('pword')
    
    if uname == 'admin' and pword == 'admin':
        return render_template('home.html', ledState = str(ledState), reply = reply)


@app.route('/home', methods=['GET','POST'])
def home(request):
    global reply, ledState
    if request.method == 'POST':
        user_input = request.form.get('input')
        reply = user_input
    return render_template('home.html', ledState = ledState, reply = reply)

@app.route('/led',methods=['GET', 'POST'])
def led(request):
    global reply,ledState
    ledState = not ledState
    onboard.value(ledState)
    return render_template('home.html', ledState = ledState, reply = reply)


@app.route('/shutdown')
def close(request):
    request.app.shutdown()
    return 'shutting down...'

def main_loop():
    while True:
        print('heartbeat')
        utime.sleep(1)

# THREAD = _thread.start_new_thread(main_loop,())
app.run(port=80)