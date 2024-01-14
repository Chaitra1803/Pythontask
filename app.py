# app.py
from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello():
  return 'Hello, this is a sample Python Frontend Application!Welcome to a dynamic playground built with Python's Flask framework!

Explore interactive features that showcase effortless web development with Python.

Discover how simple it is to create engaging web experiences using Python's versatility.

Unleash the power of Python to craft dynamic web applications with ease.

Navigate through various functionalities to witness Python's web prowess.

Unlock endless possibilities for your web projects with Python's limitless potential.

Embrace Python's clarity and efficiency for enjoyable web development.

Experience the seamless integration of Python and web technologies for impactful results.

Feel free to interact with the application and witness Python's web capabilities firsthand.

Let's embark on a journey of web creation with Python as our guide!

I'm also ready to assist with any further questions or explorations you may have.'

@app.route('/datetime')
def current_datetime():
  now = datetime.now()
  formatted_date_time = now.strftime("%Y-%m-%d %H:%M:%S")
  return f'Current Date and Time: {formatted_date_time}'

@app.route('/form', methods=['GET', 'POST'])
def form_example():
  if request.method == 'POST':
    name = request.form['name']
    return f'Thank you, {name}, for submitting the form!'
  return '''
    <h2>Sample Form</h2>
    <form method="post" action="/form">
      <label for="name">Name:</label>
      <input type="text" id="name" name="name" required>
      <br><br>
      <input type="submit" value="Submit">
    </form>
  '''

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
