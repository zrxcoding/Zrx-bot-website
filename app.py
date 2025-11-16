from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = 'YOUR_SECRET_KEY'

USERNAME = "admin"
PASSWORD = "password123"

@app.route('/')
def home():
    if session.get('logged_in'):
        return render_template('home.html')
    else:
        return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        u = request.form.get('username')
        p = request.form.get('password')
        if u == USERNAME and p == PASSWORD:
            session['logged_in'] = True
            return redirect(url_for('home'))
        else:
            error = "Invalid Credentials"
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session['logged_in'] = False
    return redirect(url_for('login'))

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    message = ""
    if request.method == 'POST':
        f = request.files.get('botfile')
        if not f:
            message = "No file selected"
        else:
            filename = f.filename
            f.save(os.path.join("uploads", filename))
            message = f"File {filename} uploaded successfully!"
    return render_template('upload.html', message=message)

if __name__ == '__main__':
    os.makedirs("uploads", exist_ok=True)
    app.run(host="0.0.0.0", port=5000)
