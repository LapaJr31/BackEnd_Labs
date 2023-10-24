from flask import Flask, jsonify 
#from flask_restful import Api, Resource
import healthCheck
import users

app = Flask(__name__)
#api = Api(app)

app.register_blueprint(healthCheck.healthy)

usersDict = users.dictUsers()
userJson = users.usersToJson(usersDict)


@app.route("/helloWorld")
def hello():
    return "Hello World!"

@app.route('/getUser', methods=['GET'])
def getUser():
    return jsonify(userJson)  



