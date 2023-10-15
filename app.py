from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://anmol70806:anmol70806@cluster0.nxvtsda.mongodb.net/sensor?retryWrites=true&w=majority"
mongo = PyMongo(app)


@app.route("/")
def hello_world():
    return "<h1>Hello, World</h1>"
@app.route("/yourendpoint", methods=['POST', 'GET'])
def receive_data():
    try:
        if request.method == 'POST':
            data = request.get_json()
            # Store the data in MongoDB
            mongo.db.sensordata.insert_one(data)
            return jsonify({"message": "Data received and stored successfully"}), 201
        elif request.method == 'GET':
            sensorval1 = request.args.get('sensorval1')
            if sensorval1 is not None:
                # Create a data dictionary with sensorval1
                data = {"sensorval1": sensorval1}
                # Store the data in MongoDB
                mongo.db.sensordata.insert_one(data)
                response = Response("Data received and stored successfully", status=201)
                response.headers['Connection'] = 'keep-alive'
                return response
            else:
                return jsonify({"error": "sensorval1 parameter is missing in the GET request"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
# @app.route("/yourendpoint", methods=['POST','GET'])
# def receive_data():
#     try:
#         data = request.get_json()

#         # Store the data in MongoDB
#         mongo.db.sensordata.insert_one(data)

#         return jsonify({"message": "Data received and stored successfully"}), 201
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

if __name__=="__main__":
    app.run(host="0.0.0.0")
