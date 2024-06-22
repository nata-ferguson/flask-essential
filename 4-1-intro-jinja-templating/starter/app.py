from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    user = {'username': 'Natasha'}
    return render_template('index.html', title='Welcome', user=user)

if __name__ == '__main__':
    app.run(debug=True)
