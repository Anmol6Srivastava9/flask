from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://anmol70806:anmol70806@cluster0.nxvtsda.mongodb.net/sensor?retryWrites=true&w=majority"
mongo = PyMongo(app)


@app.route("/")
def hello_world():
    return "<h1>Hello, World</h1>"

@app.route("/yourendpoint", methods=['POST','GET'])
def receive_data():
    try:
        data = request.get_json()

        # Store the data in MongoDB
        mongo.db.sensordata.insert_one(data)

        return jsonify({"message": "Data received and stored successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__=="__main__":
    app.run(host="0.0.0.0")
