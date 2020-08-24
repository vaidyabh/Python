from flask import Flask, jsonify, request

app = Flask(__name__)

stores =[
    {
        'name':'Mandi - 1',
        'items' : [
            {
                'name':'item1',
                'price':13
            }
        ]
    }
]

@app.route('/')
def app_start():
    return 'WELCOME To Hadoop Tech'

# Create a store
@app.route('/store', methods = ['POST'])
def create_store():
    req = request.json_data()
    new_store = {
        'name':req['name'],
        'items':[]
    }
    stores.append(new_store)
    return jsonify(new_store)

# Get a specific store
@app.route('/store/<string:name>') # By default Flask invoke the GET method
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
        
    return jsonfy({'message' : 'store not found'})

# Get a specific store
@app.route('/store')
def get_stores():
    return jsonify({'stores':stores})

# Post a item to the store
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item(name):
    for store in stores:
        if store['name'] : name:
            req = request.json_data()
            new_item = {
                'name'=req['name'],
                'price'=req['price']
            }
            items.append(new_item)
            return jsonfy(new_item)
        return jsonfy({'message':'Unable to add item to the store'})
# get an item
@app.route('/store/<string:name>/item')
def get_item(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store['items'])
        
    return jsonify({'message' : 'Items not found'})



app.run(port=12346)