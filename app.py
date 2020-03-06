from flask import Flask, jsonify, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def init():
    data = request.get_json()
    token_data = {'Authorization': f'Token {data["token"]}'}

    api_response = requests.get(
        'https://lambda-treasure-hunt.herokuapp.com/api/adv/init',
        headers=token_data
    ).json()

    return jsonify(api_response), 200

@app.route('/travel', methods=['POST'])
def travel():
    data = request.get_json()
    token_data = {'Authorization': f'Token {data["token"]}'}

    move_data = {'direction': data['direction']}

    if 'next_room_id' in data:
        move_data['next_room_id'] = data['next_room_id']

    api_response = requests.post(
        'https://lambda-treasure-hunt.herokuapp.com/api/adv/move',
        data=json.dumps(move_data),
        headers=token_data
    ).json()

    return jsonify(api_response), 200

@app.route('/pickup', methods=['POST'])
def pickup():
    data = request.get_json()
    token_data = {'Authorization': f'Token {data["token"]}'}

    item_data = {'name': 'treasure'}

    api_response = requests.post(
        'https://lambda-treasure-hunt.herokuapp.com/api/adv/take',
        data=json.dumps(item_data),
        headers=token_data
    ).json()

    return jsonify(api_response), 200

@app.route('/sell', methods=['POST'])
def sell():
    data = request.get_json()
    token_data = {'Authorization': f'Token {data["token"]}'}

    item_data = {"name":"treasure", "confirm":"yes"}

    api_response = requests.post(
        'https://lambda-treasure-hunt.herokuapp.com/api/adv/sell',
        data=json.dumps(item_data),
        headers=token_data
    ).json()

    return jsonify(api_response), 200

@app.route('/status')
def status():
    data = request.get_json()
    token_data = {'Authorization': f'Token {data["token"]}'}
    
    api_response = requests.post(
        'https://lambda-treasure-hunt.herokuapp.com/api/adv/status',
        headers=token_data
    ).json()

    return jsonify(api_response), 200

