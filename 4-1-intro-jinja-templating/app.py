from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    user = {'username': 'Natasha'}
    current_time = datetime.now().hour
    greeting = "Good morning" if current_time < 12 else "Good afternoon" if current_time < 18 else "Good evening" 
    return render_template('index.html', title='Home', user=user, greeting=greeting)

if __name__ == '__main__':
    app.run(debug=True)
