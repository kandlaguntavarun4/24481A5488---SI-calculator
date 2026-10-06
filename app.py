from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to the Flask App! <=>routing"

@app.route('/greet/<username>')
def greet(username):
    return f"Hello Good Morning, {username}!"

@app.route('/delete/<int:roll>')
def delete_user(roll):
    return redirect(url_for('greet', username='guest'))

@app.route('/calculate', methods=['GET', 'POST'])
@app.route('/calculator', methods=['GET', 'POST'])
def si():
    result = None
    if request.method == 'POST':
        try:
            principal = float(request.form.get('p', 0))
            time = float(request.form.get('t', 0))
            rate = float(request.form.get('r', 0))
            result = (principal * time * rate) / 100
        except (TypeError, ValueError):
            result = 'Invalid input'
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True, port=3500)