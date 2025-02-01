from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    html = """
    <html>
    <head>
        <meta http-equiv="refresh" content="2;url=/start">  <!-- Redirect to /start after 2 seconds -->
    </head>
    <body>
        <h1>Starting the game...</h1>
    </body>
    </html>
    """
    return html

@app.route('/start')
def start_game():
    exec(open('Start-Game.py').read())
    return "Game Started!"


if __name__ == '__main__':
    app.run()