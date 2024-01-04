from flask import Flask,request
from application.database import db
from application.config import LocalDevelopmentConfig
from flask_restful import Api, Resource, reqparse, abort

app=Flask(__name__, template_folder='templates')
app.secret_key = 'easy-grocery'

app.config.from_object(LocalDevelopmentConfig)
db.init_app(app)
app.app_context().push()
from application.controllers import *
db.create_all()
print("Created")


from application.api import *


if __name__=='__main__':
    app.run(host='0.0.0.0',port=8080)