# app.py
from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello():
  return 'Hello, this is a sample Python Frontend Application! Welcome'
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
    return render_template('form.html')  # Render the form.html template

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
