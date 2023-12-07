# app.py

from flask import Flask, render_template, request, jsonify
import redis

def create_app():
    app = Flask(__name__)
    redis_db = redis.StrictRedis(host='localhost', port=6379, db=0)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/store_data', methods=['POST'])
    def store_data():
        key = request.form['key']
        value = request.form['value']
        if key and value:
            redis_db.set(key, value)
            return jsonify({'message': 'Data stored successfully'})
        else:
            return jsonify({'error': 'Key or value is missing'})

    @app.route('/retrieve/<key>', methods=['GET'])
    def retrieve_data(key):
        value = redis_db.get(key)
        if value:
            return jsonify({key: value.decode('utf-8')})
        else:
            return jsonify({'error': 'Key not found'})

    return app

if __name__ == '__main__':
    create_app().run(debug=True, host='0.0.0.0')

