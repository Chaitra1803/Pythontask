from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, this is a sample Python Frontend Application! Welcome to the world of Flask development. Explore and create amazing web experiences!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
