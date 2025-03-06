from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
from network_scanner import scan_network

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    ip_range = request.form.get('ip_range')
    devices = scan_network(ip_range)
    for device in devices:
        send_alert(f"New device detected: {device['ip']} - {device['mac']}")
    return {'devices': devices}

def send_alert(message):
    socketio.emit('new_alert', {'message': message}, namespace='/')

if __name__ == '__main__':
    socketio.run(app, debug=True)
