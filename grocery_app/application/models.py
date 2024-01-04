from .database import db


class Customer(db.Model):
    __tablename__ = 'customers'
    
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    cart = db.relationship("Cart", back_populates="customer")
    orders = db.relationship("Orders", back_populates="customer")

    def __repr__(self):
        return f"User(name='{self.name}', username='{self.username}',email='{self.email}',password='{self.password}',phone='{self.phone}',address='{self.address}')"

class StoreManager(db.Model):
    __tablename__ = 'store_managers'
    
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    store_name = db.Column(db.String(100), unique=True, nullable=False)
    address = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    categories = db.relationship("ItemCategory", back_populates="manager")
    orders = db.relationship("Orders", back_populates="manager")
    
    def __repr__(self):
        return f"User(name='{self.name}',store_name='{self.store_name}', username='{self.username}',email='{self.email}',password='{self.password}',phone='{self.phone}',address='{self.address}')"



class Item(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer,autoincrement=True, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    unit = db.Column(db.String, nullable=False)
    seller = db.Column(db.String(100), nullable=False)
    manufacture_date = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('item_categories.id'))
    category = db.relationship('ItemCategory', back_populates='items')

    def __repr__(self):
        return f"Item(name='{self.name}', price={self.price})"



class ItemCategory(db.Model):
    __tablename__ = 'item_categories'

    id = db.Column(db.Integer,autoincrement=True, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    manager_id = db.Column(db.Integer, db.ForeignKey('store_managers.id'))
    manager = db.relationship('StoreManager', back_populates='categories')
    items = db.relationship("Item", back_populates="category",cascade="all, delete-orphan")

    def __repr__(self):
        return f"<ItemCategory(name='{self.name}')>"
    
class Cart(db.Model):
    __tablename__ = 'cart'
    
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    item_id=db.Column(db.Integer,unique=True, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'),nullable=False)
    customer = db.relationship('Customer', back_populates='cart')
    quantity=db.Column(db.Float, nullable=False)
    price = db.Column(db.Float, nullable=False)
    unit = db.Column(db.String, nullable=False)

class Orders(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    item_id = db.Column(db.Integer,nullable=False)
    item_name=db.Column(db.String(100), nullable=False)
    order_date = db.Column(db.String(100), nullable=False)
    quantity=db.Column(db.Float, nullable=False)
    price = db.Column(db.Float, nullable=False)
    unit = db.Column(db.String, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'),nullable=False)
    customer = db.relationship('Customer', back_populates='orders')
    manager_id = db.Column(db.Integer, db.ForeignKey('store_managers.id'),nullable=False)
    manager =  db.relationship('StoreManager', back_populates='orders')
