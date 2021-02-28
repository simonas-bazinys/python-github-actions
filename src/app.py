from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<img src='https://i.gifer.com/1ws.gif'>"



if __name__ == "__main__":
    app.run()



