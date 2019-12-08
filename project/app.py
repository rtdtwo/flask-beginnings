from flask import Flask

app = Flask(__name__)

@app.route('/greetings')
def greetings():
    return "May the force be with you!"

app.run()