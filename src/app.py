from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<img src='https://i.gifer.com/1ws.gif'><img src='https://beingabitchblog.files.wordpress.com/2017/11/you-can-do-it-gif-4.gif'><img src='https://media1.giphy.com/media/3oFzlUxAjIc3JvQvJK/giphy.gif'><img src='https://media4.giphy.com/media/82wOb7Qg9KuUvtdN3v/giphy.gif'>"



if __name__ == '__main__':
    app.run()



