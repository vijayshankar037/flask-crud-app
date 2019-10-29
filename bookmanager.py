import os

#Import the flask
from flask import Flask

#import the render_template
from flask import render_template

#Import request for HTTP methods
from flask import request

# include this import at the tomb
#from flask import jsonify

#Sqllite database adpter
from flask_sqlalchemy import SQLAlchemy

#Connection to database
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir,"bookdatabase.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)

#route decorator
@app.route('/', methods=['GET','POST'])  #GET
def home():
    #return "First app"
    if request.form:
        print(request.form)
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=False)
