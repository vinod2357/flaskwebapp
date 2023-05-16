from flask import Flask

app = Flask(_name_)

@app.route('/home')
def home():
    return "Hello Vinod"