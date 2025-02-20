from flask import request, session, render_template, redirect
from server import app

@app.route("/")
def index():
    return render_template(
        'dashboard.html',
        aiAgent_uuid="123456789"
    )

@app.route("/chat")
def chat():
    return render_template(
        'chat.html'
    )

@app.route("/blank")
def blank():
    return render_template(
        'blank.html'
    )
