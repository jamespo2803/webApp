from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Home Page"

@app.route("/hello")
def helloWorld():
    return "Hello World!"

@app.route("/members/<string:name>/")
def getMember(name):
    return name

if __name__ == "__main__":
    app.run()