from flask import Flask, jsonify, request
from src.models.signup import Signup
from src.extensions import db

app = Flask(__name__)

@app.route('/signups', methods=['POST'])
def create_signup():
    data = request.get_json()
    new_signup = Signup(**data)
    db.session.add(new_signup)
    db.session.commit()
    return jsonify(new_signup.to_dict()), 201

@app.route('/signups/<int:signup_id>', methods=['GET'])
def get_signup(signup_id):
    signup = Signup.query.get_or_404(signup_id)
    return jsonify(signup.to_dict())

@app.route('/signups/<int:signup_id>', methods=['PUT'])
def update_signup(signup_id):
    data = request.get_json()
    signup = Signup.query.get_or_404(signup_id)
    for key, value in data.items():
        setattr(signup, key, value)
    db.session.commit()
    return jsonify(signup.to_dict())

@app.route('/signups/<int:signup_id>', methods=['DELETE'])
def delete_signup(signup_id):
    signup = Signup.query.get_or_404(signup_id)
    db.session.delete(signup)
    db.session.commit()
    return jsonify({'message': 'Signup deleted'}), 204

if __name__ == '__main__':
    app.run(debug=True)