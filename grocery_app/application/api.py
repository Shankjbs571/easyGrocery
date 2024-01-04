from flask import current_app as app
from flask import Flask,request
from application.database import db
from flask_restful import Api, Resource, reqparse, abort
from application.controllers import *

api = Api(app)

# Argument Parsing Setup
item_parser = reqparse.RequestParser()
item_parser.add_argument("name", type=str, required=True, help="Name of the Item")
item_parser.add_argument("price", type=float, required=True, help="Price of the Item")
item_parser.add_argument("unit", type=str, required=True, help="Unit of the Item")
item_parser.add_argument("seller", type=str, required=True, help="Seller of the Item")
item_parser.add_argument("manufacture_date", type=str, required=True, help="Manufacture Date of the Item")
item_parser.add_argument("quantity", type=int, required=True, help="Quantity of the Item")
item_parser.add_argument("category_id", type=int, required=True, help="ID of the Item Category")

category_parser = reqparse.RequestParser()
category_parser.add_argument("name", type=str, required=True, help="Name of the Item Category")
category_parser.add_argument("manager_id", type=int, required=True, help="ID of the Store Manager")

# API Endpoints
class ItemAPI(Resource):
    def get(self, item_id=None):
        if item_id:
            item = Item.query.get(item_id)
            if not item:
                return {}, 404
            return {
                "id": item.id,
                "name": item.name,
                "price": item.price,
                "unit": item.unit,
                "seller": item.seller,
                "manufacture_date": item.manufacture_date,
                "quantity": item.quantity,
                "category_id": item.category_id
            }, 200
        else:
            items = Item.query.all()
            result = [{
                "id": item.id,
                "name": item.name,
                "price": item.price,
                "unit": item.unit,
                "seller": item.seller,
                "manufacture_date": item.manufacture_date,
                "quantity": item.quantity,
                "category_id": item.category_id
            } for item in items]
            return result, 200

    def post(self):
        args = item_parser.parse_args()
        item = Item(
            name=args['name'],
            price=args['price'],
            unit=args['unit'],
            seller=args['seller'],
            manufacture_date=args['manufacture_date'],
            quantity=args['quantity'],
            category_id=args['category_id']
        )
        db.session.add(item)
        db.session.commit()
        return {
            "id": item.id,
            "name": item.name,
            "price": item.price,
            "unit": item.unit,
            "seller": item.seller,
            "manufacture_date": item.manufacture_date,
            "quantity": item.quantity,
            "category_id": item.category_id
        }, 201

    def put(self, item_id):
        item = Item.query.get(item_id)
        if not item:
            return {}, 404

        args = item_parser.parse_args()
        item.name = args['name']
        item.price = args['price']
        item.unit = args['unit']
        item.seller = args['seller']
        item.manufacture_date = args['manufacture_date']
        item.quantity = args['quantity']
        item.category_id = args['category_id']
        db.session.commit()
        return {
            "id": item.id,
            "name": item.name,
            "price": item.price,
            "unit": item.unit,
            "seller": item.seller,
            "manufacture_date": item.manufacture_date,
            "quantity": item.quantity,
            "category_id": item.category_id
        }, 200

    def delete(self, item_id):
        item = Item.query.get(item_id)
        if not item:
            return {}, 404
        db.session.delete(item)
        db.session.commit()
        return {}, 204


class ItemCategoryAPI(Resource):
    def get(self, category_id=None):
        if category_id:
            category = ItemCategory.query.get(category_id)
            if not category:
                return {}, 404
            return {"id": category.id, "name": category.name, "manager_id": category.manager_id}, 200
        else:
            categories = ItemCategory.query.all()
            result = [{"id": category.id, "name": category.name, "manager_id": category.manager_id} for category in categories]
            return result, 200

    def post(self):
        args = category_parser.parse_args()
        category = ItemCategory(name=args['name'], manager_id=args['manager_id'])
        db.session.add(category)
        db.session.commit()
        return {"id": category.id, "name": category.name, "manager_id": category.manager_id}, 201

    def put(self, category_id):
        category = ItemCategory.query.get(category_id)
        if not category:
            return {}, 404

        args = category_parser.parse_args()
        category.name = args['name']
        category.manager_id = args['manager_id']
        db.session.commit()
        return {"id": category.id, "name": category.name, "manager_id": category.manager_id}, 200

    def delete(self, category_id):
        category = ItemCategory.query.get(category_id)
        if not category:
            return {}, 404
        db.session.delete(category)
        db.session.commit()
        return {}, 204

# API Resource Routing
api.add_resource(ItemAPI, "/api/item", "/api/item/<int:item_id>")
api.add_resource(ItemCategoryAPI, "/api/itemcategory", "/api/itemcategory/<int:category_id>")