from flask import abort, jsonify, request
from flask_restful import  Resource
from .models import Product,products, Sale, sales, User,users


class Products(Resource):
    """This class provides access to operations to GET and POST on products"""

    def get(self):
        """GETs all products"""
        return jsonify({"Products": products,
                        "status":200})

    def post(self):
        """Saves a new product item"""
        product_name = request.get_json("product_name")["product_name"].strip(" ")
        product_price = request.get_json("product_price")["product_price"]
        quantity = request.get_json("quantity")["quantity"]
        min_quantity = request.get_json("min_quantity")["min_quantity"]
        
        if not product_name or product_name=="" or not product_price :
            abort(400)

        if not request.json:
            abort(400)

        product = Product(product_name, product_price, quantity, min_quantity)
        newproduct = product.save_product()
        return jsonify({"Message":"Successfully saved",
                        "Product id saved": newproduct,
                        "status": 201})
    
class Sales(Resource):
    """This class provides access to operations to GET and POST on sales"""

    def get(self):
        """Gets all sales orders"""
        return jsonify({"Sales": sales,
                        "status":200})

    def post(self):
        """Saves a new sales order"""
        # sale_id = uuid.uuid1()
        product_name = request.get_json("product_name")["product_name"].strip(" ")
        product_price = int(request.get_json("product_price")["product_price"])
        quantity = int(request.get_json("quantity")["quantity"])
        attendant = request.get_json("attendant")["attendant"].strip(" ")
        total_price = product_price * quantity
       
        if product_name=="" or not product_name:
            abort(400)
        
        if not request.json:
            abort(400)

        product_available = [product for product in products if product_name == product["product_name"]]

        excess_order = [product for product in product_available if quantity > (product["quantity"] - product["min_quantity"])]

        if len(product_available) == 0:
            # abort(400)
            return jsonify({"message":"Product not available",
                            "status":404})
        elif len(excess_order) > 0:
            return jsonify({"message":"Forbidden: There are fewer products than requested",
                            "status":403})
        else:
            sale = Sale(product_name, product_price, quantity, total_price, attendant)
            newsale = sale.save_sale()
            return jsonify({"Message":"Successfully saved",
                            "Sale recorded": newsale,
                            "status": 201})


class Users(Resource):
    """This class provides access to operations to GET and POST on users"""

    def get(self):
        """Gets all users"""
        return jsonify(users)

    def post(self):
        """Saves a new user"""
        f_name = request.get_json("f_name")["f_name"].strip(" ")
        s_name = request.get_json("s_name")["s_name"].strip(" ")
        email = request.get_json("email")["email"].strip(" ")
        password = request.get_json("password")["password"].strip(" ")
        role = request.get_json("role")["role"].strip(" ")

        user = User(f_name,s_name,email, password, role)
        newuser = user.save_user()
        return jsonify({"Message":"Successfully saved",
                        "User saved": newuser,
                        "status": 201})


class SingleProduct(Resource):
    """This resource will be used to retrieves a single product"""
    def get(self, product_id):
        """Gets a single product"""
        if not product_id or not isinstance(product_id, int):
            abort(404)		
        product = [product for product in products if product["product_id"] == product_id]
        if len(product) == 0:
            return jsonify({"Message": "No product found",
			    "status":404})
        return jsonify({"Product" : product,
            "status" : 200})

class SingleSale(Resource):
    """This resource will be used by the api to fetch specific sale"""

    def get(self, sale_id):
        """Gets a single sale order"""
        if not isinstance(sale_id, int) or not sale_id:
            abort(404)
        sale  = [sale for sale in sales if sale_id == sale["sale_id"]]
        if len(sale) == 0:
            return jsonify({"message":"Sale not found",
                            "status": 404})
        else:
            return jsonify({"Sale" : sale,
                            "status" : 200})

class SingleUser(Resource):
    """This resource will be used by the api to fetch specific sale"""

    def get(self, user_id):
        """Gets a single user"""
        if not user_id:
            abort(404)
        user  = [user for user in users if user_id == user["user_id"]]
        if len(user) == 0:
            return jsonify({"message":"User not found",
                            "status": 404})
        return jsonify({"User" : user,
                        "status" : 200})
