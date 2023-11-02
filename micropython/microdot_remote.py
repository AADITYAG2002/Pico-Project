from lib.microdot import Microdot, Response
from lib.microdot_utemplate import render_template

app = Microdot()
Response.default_content_type = 'text/html'

@app.route('/', methods=['GET', 'POST'])
def index(request):
    name = None
    if request.method == 'POST':
        name = request.form.get('name')
    return render_template('index.html', name = name)

@app.route('/login')
def login(request):
    return "Come back..."

@app.route('/shutdown')
def close(request):
    request.app.shutdown()
    return 'shutting down...'

app.run(port=80)