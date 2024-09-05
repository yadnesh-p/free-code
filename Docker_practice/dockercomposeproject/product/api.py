from flask import Flask
from flask_restful import Resource,Api

#create a flask object
app = Flask(__name__)
api = Api(app)

#Creating a class of fruits that will hold the accessorrs
class Fruits(Resource):
    def get(self):
        #returns a dictionry with fruits
        return {'fruit':['Mango','Pomegranate','Orange','Litchi']}

#adds the resources at the root route
api.add_resource(Fruits,'/')

#if this file is expected then run the service
if __name__ == '__main__':
    #run the service
    app.run(host='0.0.0.0',port=80,debug=True)
