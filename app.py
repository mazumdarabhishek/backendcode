from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from restaurant_db_actions import restaurantDbQuery
from datetime import  datetime
from flask_cors import CORS
from restaurant_OrderDB_actions import OrderDbQuery
import json

app = Flask(__name__)
CORS(app)
api = Api(app)
app.secret_key = "9977701001573a1c28123a15952f53c1"
app.config['CORS_HEADERS'] = 'Content-Type'
obj = restaurantDbQuery()
obj2 = OrderDbQuery()

class restaurant(Resource):

    def post(self):
        data = request.get_json()
        now = datetime.now()
        now = now.strftime("%Y-%m-%d %H:%M:%S")


        msg = obj.New_Entry(
                data['restaurantname'],
                data['fssailicno'],
                data['gstin'],
                data['cgst'],
                data['sgst'],
                data['restaurantphone'],
                data['restaurantemail'],
                data['restaurantaddress'],
                data['restaurantmembershipstatus'],
                now)

        return {"message": msg}

class restaurantopr(Resource):
    def get(self,id_):

        data = obj.fetch_data(id_)

        return {"Data": data}, 400


    def put(self,id_):
        data  = request.get_json()
        print(data)
        msg = obj.update_entry(id_, data)
        return {"message": msg}

    def delete(self,id_):
        msg = obj.remove_entry(id_)
        return {"message":msg}

class restaurantdata(Resource):

    def get(self):

        data = obj.fetch_all()

        return {"Data": data}

class orders(Resource):
    def post(self):
        data = request.get_json()
        # inserting data into DB
        # for loop for multiple json
        # for i in data:
        msg = obj2.createOrder(data)
        return {"message": msg}
class orderlist(Resource):

    def get(self,orderid):
        orderid = str(orderid)
        msg = obj2.fetchAllOrders(orderid)
        return {"data": msg}


api.add_resource(restaurant, "/restaurant/create")
api.add_resource(restaurantopr, "/restaurantopr/<string:id_>")
api.add_resource(restaurantdata, "/restaurantdata")
api.add_resource(orders, "/orders")
api.add_resource(orderlist, "/orderlist/<string:orderid>")

if __name__ == "__main__":

    app.run(debug=True, port=5000)





