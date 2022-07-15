from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello! I'm a webserver serving for Topicmaker Discord bot."

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()