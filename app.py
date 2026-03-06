from flask import Flask, render_template
app = Flask(__name__)

# Home
@app.route('/')
def index():
    return render_template("index.html")

# About
@app.route('/about')
def about():
    return render_template("about.html")

# Privacy Policy
@app.route('/privacy')
def privacy():
    return render_template("privacy.html")

# Sign Up
@app.route('/signup')
def signup():
    return render_template("signup.html")

# Login
@app.route('/login')
def login():
    return render_template("login.html")

# Logged Out
@app.route('/logout')
def logout():
    return render_template("loggedout.html")

# Profile
@app.route('/profile')
def profile():
    return render_template("profile.html")

# Easter Egg
@app.route('/easter-egg')
def easter_egg():
    return render_template("easteregg.html")

if __name__ == "__main__":
    app.run(debug=True)