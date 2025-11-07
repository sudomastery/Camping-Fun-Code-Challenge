from flask import Flask, jsonify, request
from src.models.activity import Activity
from src.extensions import db

def test_create_activity(client):
    response = client.post('/activities', json={'name': 'Hiking', 'description': 'A fun hiking activity.'})
    assert response.status_code == 201
    assert response.json['name'] == 'Hiking'

def test_get_activities(client):
    response = client.get('/activities')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_get_activity(client):
    activity = Activity(name='Swimming', description='A refreshing swimming activity.')
    db.session.add(activity)
    db.session.commit()
    
    response = client.get(f'/activities/{activity.id}')
    assert response.status_code == 200
    assert response.json['name'] == 'Swimming'

def test_update_activity(client):
    activity = Activity(name='Fishing', description='A relaxing fishing activity.')
    db.session.add(activity)
    db.session.commit()
    
    response = client.put(f'/activities/{activity.id}', json={'name': 'Updated Fishing', 'description': 'Updated description.'})
    assert response.status_code == 200
    assert response.json['name'] == 'Updated Fishing'

def test_delete_activity(client):
    activity = Activity(name='Camping', description='A fun camping activity.')
    db.session.add(activity)
    db.session.commit()
    
    response = client.delete(f'/activities/{activity.id}')
    assert response.status_code == 204
    
    response = client.get(f'/activities/{activity.id}')
    assert response.status_code == 404