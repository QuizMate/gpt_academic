from flask import Flask, render_template, request, redirect, url_for, session
import config
app = Flask(__name__)
app.config.from_object(config)

@app.route('/')
def index():
    return render_template('./index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('./dashboard.html')


if __name__ == '__main__':
    app.run()