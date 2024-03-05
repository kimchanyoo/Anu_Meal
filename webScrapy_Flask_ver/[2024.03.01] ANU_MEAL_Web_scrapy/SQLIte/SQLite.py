from flask import Flask,jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root'

@app.route('/')
def index():
    return jsonify({"key":"hello"})

if __name__ == '__main__':
    app.run(debug=True)