from flask import Flask, render_template, request, redirect
from todo_app.data.trello_items import get_items, add_item, move_to_do, move_doing, move_done
from todo_app.flask_config import Config


app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    return render_template("index.html", items=get_items())


@app.route('/add', methods=['POST'])
def add():
    add_item(request.form.get('description'))
    return redirect('/')


@app.route('/todo/<id>', methods=['POST'])
def todo(id):
    move_to_do(id)
    return redirect('/')


@app.route('/doing/<id>', methods=['POST'])
def doing(id):
    move_doing(id)
    return redirect('/')


@app.route('/done/<id>', methods=['POST'])
def done(id):
    move_done(id)
    return redirect('/')