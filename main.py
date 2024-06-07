from sqlalchemy import create_engine , ForeignKey , Column , String , Integer , CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from flask import Flask , render_template , request
from blueprints.people_blueprint import people_bp
from blueprints.insert_blueprint import insert_bp
app = Flask (__name__, template_folder='templates')



try :
    app.register_blueprint(people_bp, url_prefix='/')
    app.register_blueprint(insert_bp, url_prefix='/insert')



    app.run(host = "0.0.0.0" , port = 80,debug=True)
except :
    print("connection failed")
