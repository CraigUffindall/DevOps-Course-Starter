from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

from todo_app.data.session_items import get_items
from todo_app.data.session_items import add_item
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