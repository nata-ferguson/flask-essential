from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    user = {'username': 'natasha', 'is_admin': True}
    articles = ['Article 1', 'Article 2', 'Article 3']
    return render_template('index.html', user=user, articles=articles)

if __name__ == '__main__':
    app.run(debug=True)
