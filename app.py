from flask import Flask

# Adding name
app = Flask(__name__)

# Root
@app.route('/')
def hello_world():
    return 'Hello world'
