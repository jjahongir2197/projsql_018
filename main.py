from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///files.db'
app.config['UPLOAD_FOLDER'] = 'uploads'

db = SQLAlchemy(app)

class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(200))

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']

    path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(path)

    f = File(filename=file.filename)
    db.session.add(f)
    db.session.commit()

    return "Uploaded"

with app.app_context():
    db.create_all()
