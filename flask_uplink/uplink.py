
from functools import wraps
from flask import request, current_app, g, Blueprint

from flask_socketio import SocketIO
from flask_socketio import Namespace, emit

html_wrapper = """<head><script src="//cdnjs.cloudflare.com/ajax/libs/socket.io/2.2.0/socket.io.js" integrity="sha256-yr4fRk/GU1ehYJPAs8P4JlTgu0Hdsp4ZKrx8bDEDC3I=" crossorigin="anonymous"></script>
<script type="text/javascript" charset="utf-8">
    var socket = io();
    console.log(socket)
    socket.on('connect', function() {
        socket.emit('message', null);
    });
    socket.on('update_content', function(data) {
        document.querySelector('#_content').innerHTML = data
        addEventables()
    });

    function addEventables() {
        let eventables = document.querySelectorAll('[uplink-event]')
        for (let i=0; i< eventables.length;i++) {
            let eventable = eventables[i]
            eventable.addEventListener('click', function(e) {
                socket.emit(e.target.getAttribute('uplink-event'), 1);
            })
        }
    }
</script></head><body>
<div id="_content">Initializing...</div></body>
"""


class Uplink(object):
    def __init__(self,app=None, secret="top_secret_1!"):
        self.app = app
        self.app.config['SECRET_KEY'] = secret
        self.sio = SocketIO(self.app)
        self.initialized = False
        self.sio.on_event('connect', self.update_render, namespace='/')
        self.func = None
        self.funcs = {}

    def update_render(self):
        if not self.func:
            return 
        emit('update_content', self.func())

    def render(self):
        def dec(f):
            @wraps(f)
            def wrapper(*msg):
                self.func = f
                if not self.initialized:
                    self.initialized = True
                    return html_wrapper
                return emit('update_content', f())
            return wrapper
        return dec

    def event(self, channel_id):
        def test(burp):
            if channel_id not in self.funcs:
                print("No func found")
                return
            self.funcs[channel_id]()
            emit('update_content', self.func())

        self.sio.on_event(channel_id, test, namespace='/')
        def dec(f):
            self.funcs[channel_id] = f
        return dec

    def run(self):
        self.sio.run(self.app)