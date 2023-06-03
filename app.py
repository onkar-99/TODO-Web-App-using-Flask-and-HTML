from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'juhiSecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(100), nullable = False)
    date = db.Column(db.Date, nullable = False)
    due_date = db.Column(db.Date, nullable = False)
    def __repr__(self):
        return f'{self.title} created on {self.date}'
    
with app.app_context():
    db.create_all()
    
from routes import *

if __name__ == '__main__':
    app.run(debug=True)