from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    password = request.form.get("password")
    
    if password == "zrx123":  # Password yaha change kar sakta hai
        return render_template("dashboard.html")
    else:
        return "Invalid Password ❌"

@app.route("/start-bot")
def start_bot():
    return "Bot Started Successfully 🚀 (Future feature)"

if __name__ == "__main__":
    app.run()