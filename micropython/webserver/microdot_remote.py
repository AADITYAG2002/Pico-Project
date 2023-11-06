from lib.microdot import Microdot, Response, redirect
from lib.microdot_utemplate import render_template
import utime, _thread

from machine import Pin
from lib.chatbot import chat

led = Pin('LED', Pin.OUT)

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
        # return render_template('home.html', ledState = None, reply = None)
        return redirect('/home')

@app.route('/home', methods=['GET','POST'])
def home(request):
    led_state = None
    reply = None
    if request.method == 'POST':
        user_input = request.form.get('input')
        reply = chat(user_input)
    return render_template('home.html', ledState = led_state, reply = reply)

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