from application import app
from application.modules.trello import Trello
import json

@app.route('/')
def login():
    return 'ok'
