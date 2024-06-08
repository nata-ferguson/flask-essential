from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    user = {'username': 'Natasha'}
    return render_template('index.html', title='Home', user=user)

if __name__ == '__main__':
    app.run(debug=True)
