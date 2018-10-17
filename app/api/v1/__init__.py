from flask import Blueprint
from flask_restful import Api
from .views import Products, Sales, Users, SingleProduct, SingleSale, SingleUser

app_blueprint = Blueprint("api", __name__, url_prefix='/api/v1')
api = Api(app_blueprint)

api.add_resource(Products, "/products")
api.add_resource(Sales, "/sales")
api.add_resource(Users, "/users")
api.add_resource(SingleProduct, "/products/<int:product_id>")
api.add_resource(SingleSale, "/sales/<int:sale_id>")
api.add_resource(SingleUser, "/users/<int:user_id>")