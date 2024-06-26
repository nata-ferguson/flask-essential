from flask import Flask, render_template, request
from forms import MyForm

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Necessary for CSRF protection

@app.route('/form', methods=['GET', 'POST'])
def form():
    form = MyForm()
    if request.method == 'POST' and form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        return render_template('success.html', name=name, email=email)
    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)

