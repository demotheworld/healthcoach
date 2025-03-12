from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello, World!'})

@app.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    # Process data and save to database (or other storage)
    return jsonify({'message': 'Item created successfully', 'data': data}), 201

@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    # Retrieve item from database based on item_id
    return jsonify({'id': item_id, 'name': f'Item {item_id}'})

if __name__ == '__main__':
    app.run(debug=False)
