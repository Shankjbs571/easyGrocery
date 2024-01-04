from flask import current_app as app
from flask import render_template, request, session, redirect, url_for, make_response
from .models import *
from templates import *
from sqlalchemy import func
import matplotlib
import io
import base64
import datetime

# Get the current date and time
current_datetime = datetime.datetime.now()

# Print the current date and time
print("Current date and time:", current_datetime)

matplotlib.use('agg')  # Use the "agg" backend
   
import matplotlib.pyplot as plt
import time
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route("/signup/customer", methods=['POST'])
def customer_signup():
    name = request.form.get('name')
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    phone = request.form.get('phone')
    address = request.form.get('address')
    
    existing_user = Customer.query.filter_by(username=username).first()
    if existing_user:
        message = "Already Exist. Please Use Different Username and Email!"
        return render_template("register.html", message=message)
    new_customer=Customer(name=name,username=username,email=email,password=password,phone=phone,address=address)
    print("NC: ", new_customer.__repr__())
    db.session.add(new_customer)
    db.session.commit()
    return redirect(url_for('home', message='Successfully Registered! Now you can login!'))

@app.route("/signup/manager", methods=['POST'])
def storeManager_signup():
    name = request.form.get('name')
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    store_name = request.form.get('store_name')
    phone = request.form.get('phone')
    address = request.form.get('address')
    
    existing_user = StoreManager.query.filter_by(username=username,store_name=store_name).first()
    if existing_user:
        message = "Either Username or Store name already Exist. Please Use something different!"
        return render_template("register.html", message=message)
    else: 
        new_StoreManager=StoreManager(name=name,username=username,email=email,password=password,store_name=store_name,phone=phone,address=address)
        print("NC: ", new_StoreManager.__repr__())
        db.session.add(new_StoreManager)
        db.session.commit()
        return redirect(url_for('home', message='Successfully Registered! Now you can login!'))
    
@app.route("/login",methods=['POST','GET'])
def login():
    if request.method=="GET":
        return render_template("login.html")
    elif request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        role = request.form.get('role')
        print("ROLE: ", role)
        if role == 'customer':
            customer = Customer.query.filter_by(username=username, password=password).first()
            print("customer ",customer)
            if customer:
                session['customer_id'] = customer.id
                print("session ",session)
                return redirect(url_for("customer_dashboard",message="Login Successful!"))
            else:
                print("inside else")
                return redirect(url_for("login",message="Wrong Username or password ! Profile Doesn't exist"))
        elif role == 'manager':
            manager = StoreManager.query.filter_by(username=username, password=password).first()
            if manager:
                session['manager_id'] = manager.id
                print("session ",session)
                return redirect(url_for("store_manager_dashboard",message="Login Successful!"))
            else:
                return redirect(url_for("login",message="Wrong Username or password ! Profile Doesn't exist"))

        return "POSTED login credentials role error!"
    
@app.route("/customer_dashboard",methods=['GET','POST'])
def customer_dashboard():
    # Ensure the user is logged in
    if "customer_id" not in session:
        return redirect("/login")  # Redirect to login page if not logged in
    customer_id=session["customer_id"]
    customer = Customer.query.filter_by(id=customer_id).first()
    cart_items = Cart.query.filter_by(customer_id=customer_id).all()
    my_orders=Orders.query.filter_by(customer_id=customer_id).all()
    item_categories = ItemCategory.query.all()
    item_list=[]
    final_amount=0
    
    if request.method == 'GET':
        print(
            "inside get customer"
        )
        for item in cart_items:
            print(f'CART-Items  id {item.id} item_id {item.item_id} customer_id {item.customer_id} quantity {item.quantity} price {item.price}')
            item_detail=Item.query.filter_by(id=item.item_id).all()
            if item_detail:
                item_copy = Item(
                id=item_detail[0].id,
                name=item_detail[0].name,
                quantity=item_detail[0].quantity,
                price=item_detail[0].price,
                unit=item_detail[0].unit
                )
                item_copy.quantity=item.quantity
                item_copy.price=item.price
                item_copy.unit=item.unit
                item_list.append(item_copy)
                final_amount+=item.price
            # print("item_detail.name ",item_detail[0].name)
               # return render_template("customer/cstmr_dashboard.html", my_orders=my_orders,customer=customer,item_categories=item_categories,cart=item_list,final_amount=final_amount)
        print("item_listcarrttt ",item_list)
        return render_template("customer/cstmr_dashboard.html", my_orders=my_orders,customer=customer,item_categories=item_categories,cart=item_list,final_amount=final_amount)
    elif request.method == 'POST':
        print("Inside customer post after order placed")
        order_status = request.form.get('order_status')
        print("$$order_status$$ ",order_status)
        if order_status == "order_confirmed":
            
            for item in cart_items:
                #print(f'CART-Items  id {item.id} item_id {item.item_id} customer_id {item.customer_id} quantity {item.quantity} price {item.price}')
                original_item=Item.query.filter_by(id=item.item_id).first()
                original_item_category=ItemCategory.query.filter_by(id=original_item.category_id).first()

                print("original_item.quantity ",original_item.quantity)
                print("cart item price ",item.price)
                original_item.quantity=original_item.quantity-item.quantity
                print("after original_item.quantity ",original_item.quantity)
                #response = requests.post('myorders',data="data")
                current_datetime = datetime.datetime.now()
                order=Orders(item_id = original_item.id, item_name=original_item.name,order_date=current_datetime,quantity=item.quantity,unit=item.unit ,price=item.price,customer_id=customer_id,manager_id=original_item_category.manager_id)
                db.session.add(order)
                db.session.delete(item) 
                db.session.commit()
                print("deleted commited")

        response = make_response()
        response.status_code = 200
        return response

@app.route("/store_manager_dashboard")
def store_manager_dashboard():
    # Ensure the user is logged in
    if "manager_id" not in session:
        return redirect("/login")  # Redirect to login page if not logged in
    # Generate data for the bar graph
    categories = []
    values = []
    
    manager = StoreManager.query.filter_by(id=session["manager_id"]).first()
    item_categories = ItemCategory.query.filter_by(manager_id=session["manager_id"]).all()
    for i in item_categories:
        values.append(len(i.items))
        categories.append(i.name)
    # Retrieve items from the database for the logged-in user
    data = list(zip(categories, values))
    plt.bar(categories, values)
    plt.xlabel('Category Names')
    plt.ylabel('Available Stock')
    plt.title('Category-wise stock')

    # Save the graph to a buffer
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    bar_graph = base64.b64encode(buffer.getvalue()).decode()

    # Clear the buffer and close the plot
    buffer.close()
    plt.clf()

    items0 = []
    quantity0 = []
    orders = Orders.query.filter_by(manager_id=session["manager_id"]).all()

    for i in orders:

        items0.append(i.item_name)
        quantity0.append(i.quantity)

    item_quantity_dict = {}
    for i in range(len(items0)):
        item_name = items0[i]
        item_qty = quantity0[i]

        # Check if the item name is already in the dictionary
        if item_name in item_quantity_dict:
            # If it exists, add the quantity to the existing value
            item_quantity_dict[item_name] += item_qty
        else:
            # If it's a new item name, add it to the dictionary with its quantity
            item_quantity_dict[item_name] = item_qty    

    items = []
    quantity = []
    for i in item_quantity_dict:
        items.append(i)
        quantity.append(item_quantity_dict[i])
    print("item_quantity_dict", item_quantity_dict)
    data2 = list(zip(items, quantity))
    # Create the bar graph
    plt.plot(items, quantity, marker='o', linestyle='-')
    plt.xlabel('Item Name')
    plt.ylabel('Sales Number')
    plt.title('Sales Data')

    # Save the graph to a buffer
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    graph_url = base64.b64encode(buffer.getvalue()).decode()

    # Clear the buffer and close the plot
    buffer.close()
    plt.clf()

    return render_template("store_manager/store_mngr_dashboard.html",
                            sold_items=orders,
                            linegraph_filename=None,
                            bar_graph=bar_graph,
                            graph_url=graph_url,
                            data=data,
                            data2=data2,
                            manager=manager,
                            item_categories=item_categories)

@app.route('/logout', methods=['GET'])
def logout():
    # Clear session data
    session.clear()
    # Redirecting to the home page with a query parameter
    return redirect(url_for('home', message='Logout successful. You have been logged out.'))

@app.route('/save_new_category', methods=['POST'])
def save_new_category():
    if request.method == "POST":
        manager_id=session['manager_id']
        new_category = request.form.get('new_category')
        print("new_category: ", new_category)
        print("Session mID: ",manager_id)
        existing_category = ItemCategory.query.filter_by(name=new_category, manager_id=manager_id).first()
        if existing_category:
            print("category already exist")
            return redirect("/store_manager_dashboard")
        else:
            new_category=ItemCategory(name=new_category, manager_id=manager_id)
            db.session.add(new_category)
            db.session.commit()
            print("Saved Successfully!")
            return redirect("/store_manager_dashboard")
        

@app.route('/delete_category/<name>')
def delete_category(name):
    manager_id=session['manager_id']
    existing_category = ItemCategory.query.filter_by(name=name, manager_id=manager_id).first()

    if existing_category:
        db.session.delete(existing_category)
        db.session.commit()
        message="Category deleted successfully"

    # Redirecting to the home page with a query parameter
    return redirect(url_for('store_manager_dashboard', message=message))

@app.route('/edit_category/<int:category_id>',methods=['POST'])
def edit_category(category_id):
    manager_id=session['manager_id']
    existing_category = ItemCategory.query.filter_by(id=category_id, manager_id=manager_id).first()
    
    category_name = request.form.get('category_name')
    existing_category.name=category_name
    db.session.commit()
    message="Category edited successfully"

    # Redirecting to the home page with a query parameter
    return redirect(url_for('store_manager_dashboard', message=message))

@app.route('/delete_item/<int:item_id>')
def delete_item(item_id):
    manager_id=session['manager_id']
    existing_item = Item.query.filter_by(id=item_id).first()

    if existing_item:
        db.session.delete(existing_item)
        db.session.commit()
        message="item deleted successfully"

    # Redirecting to the home page with a query parameter
    return redirect(url_for('store_manager_dashboard', message=message))

@app.route('/add_item/<int:category_id>',methods=['POST'])
def add_item(category_id):
    manager_id=session['manager_id']
    manager=StoreManager.query.filter_by(id=manager_id).first()
    item_name = request.form.get('item_name')
    price = request.form.get('price')
    unit = request.form.get('unit')
    manufacture_date = request.form.get('manufacture_date')
    quantity = request.form.get('quantity')
    print("item_name: ",item_name)
    print("price: ",price)
    print("unit: ",unit)
    print("quantity: ",quantity)

    new_item=Item(name=item_name,price=price,unit=unit,seller=manager.store_name, manufacture_date=manufacture_date, quantity=quantity, category_id=category_id)
    db.session.add(new_item)
    db.session.commit()
    message="item added successfully"
    print(message)
    # Redirecting to the home page with a query parameter
    return redirect(url_for('store_manager_dashboard', message=message))

@app.route('/edit_item/<int:item_id>',methods=['POST'])
def edit_item(item_id):
    manager_id=session['manager_id']
    manager=StoreManager.query.filter_by(id=manager_id).first()
    item_name = request.form.get('item_name')
    price = request.form.get('price')
    unit = request.form.get('unit')
    manufacture_date = request.form.get('manufacture_date')
    quantity = request.form.get('quantity')
    print("item_name: ",item_name)
    print("price: ",price)
    print("unit: ",unit)
    print("quantity: ",quantity)

    existing_item=Item.query.filter_by(id=item_id).first()
    existing_item.name=item_name
    existing_item.price=price 
    existing_item.unit=unit
    existing_item.manufacture_date=manufacture_date
    existing_item.quantity=quantity
    
    db.session.commit()
    message="Item updated successfully"
    print(message)
    # Redirecting to the home page with a query parameter
    return redirect(url_for('store_manager_dashboard', message=message))

@app.route('/add_to_cart/<int:item_id>', methods=['GET','POST'])
def add_to_cart(item_id):
    if request.method == 'POST':
        print("Inside Post")
        item_name = request.form.get('item_name')
        price = request.form.get('price')
        quantity = request.form.get('quantity')
        unit = request.form.get('unit1')
        print("$$$$$$$$$$$$$$ unit: ", unit)  
        print("from modal")
        print(f'item_name {item_name} price {price} quantity {quantity}')
        # return "From modal"
        customer_id=session['customer_id']
        item = Item.query.filter_by(id=item_id).first()
        existing_cart=Cart.query.all()
        print("existing_cart ",existing_cart)
        exist=False
        
        for i in existing_cart:
            if item.id == i.item_id:
                i.quantity=quantity
                exist=True
                print("i.quantity ",i.quantity)
                i.price=item.price*float(i.quantity)
                print("i.price ", i.price)
                message='Quantity Increased'
                db.session.commit()
                break
        if not exist:
            new_cart_item=Cart(item_id=item.id,customer_id=customer_id,quantity=quantity,price=item.price, unit=item.unit)
            db.session.add(new_cart_item)
            db.session.commit()
            message='Addded to Your Cart!'
        return redirect(url_for('customer_dashboard', message=message))
    else:
        customer_id=session['customer_id']
        item = Item.query.filter_by(id=item_id).first()
        existing_cart=Cart.query.all()
        print("existing_cart ",existing_cart)
        exist=False
        
        for i in existing_cart:
            if item.id == i.item_id:
                i.quantity=i.quantity+1
                exist=True
                print("i.quantity ",i.quantity)
                i.price=item.price*i.quantity
                print("i.price ", i.price)
                message='Quantity Increased'
                db.session.commit()
                break
        if not exist:
            new_cart_item=Cart(item_id=item.id,customer_id=customer_id,quantity=float('1'),price=item.price,unit=item.unit)
            db.session.add(new_cart_item)
            db.session.commit()
            message='Addded to Your Cart!'
        return redirect(url_for('customer_dashboard', message=message))


@app.route('/remove_from_cart/<int:item_id>',methods=['GET'])
def remove_from_cart(item_id):
    existing_cart_item = Cart.query.filter_by(item_id=item_id).first()
    print("quantity")
    print("price ")
    db.session.delete(existing_cart_item)
    db.session.commit()
    
    return redirect(url_for('customer_dashboard'))

# checkout item 
@app.route('/place_your_order')
def place_your_order():
    
    customer_id=session["customer_id"]
    customer = Customer.query.filter_by(id=customer_id).first()
    cart_items = Cart.query.filter_by(customer_id=customer_id).all()
    item_categories = ItemCategory.query.all()
    item_list=[]
    final_amount=0
    for item in cart_items:
        print(f'CART-Items  id {item.id} item_id {item.item_id} customer_id {item.customer_id} quantity {item.quantity} price {item.price}')
        item_detail=Item.query.filter_by(id=item.item_id).all()
        item_copy = Item(
        id=item_detail[0].id,
        name=item_detail[0].name,
        quantity=item_detail[0].quantity,
        price=item_detail[0].price,
        unit=item_detail[0].unit

        )
        item_copy.quantity=item.quantity
        item_copy.price=item.price
        item_copy.unit=item.unit
        item_list.append(item_copy)
        final_amount+=item.price
    
    return render_template('place_your_order.html',final_amount=final_amount,item_list=item_list,customer=customer)

@app.route('/search', methods=['GET', 'POST'])
def search():
    search_query = request.form.get('query')
    search_by = request.form.get('search_by')
    print("search_query ",search_query)
    print("search_by ",search_by)
    customer_id=session["customer_id"]
    customer = Customer.query.filter_by(id=customer_id).first()
    my_orders=Orders.query.filter_by(customer_id=customer_id).all()

    if search_query and search_by:
        if search_by == "1":  # Item Category
            # Apply logic to search by item category
            # Perform necessary database queries or any other processing
            item_category_list=[]
            item_categories = ItemCategory.query.all()
            for item_category in item_categories:
                if search_query.lower() in item_category.name.lower():
                    print("matched item_category ",item_category)
                    item_category_list.append(item_category)

            print("item_category_list ",item_category_list)
            return render_template('search_results.html',my_orders=my_orders,customer=customer,search_results=item_category_list,is_Category='True')   
        elif search_by == "2":  # Item
            item_list=[]
            items = Item.query.all()
            for item in items:
                if search_query.lower() in item.name.lower():
                    print("matched item ",item)
                    item_list.append(item)

            
            return render_template('search_results.html',my_orders=my_orders,customer=customer,search_results=item_list,is_Category='False')
        elif search_by == "3":  # Price
            item_list=[]
            items = Item.query.all()
            for item in items:
                if search_query in str(item.price):
                    print("matched item ",item)
                    item_list.append(item)

            
            return render_template('search_results.html',my_orders=my_orders,customer=customer,search_results=item_list,is_Category='False')
        elif search_by == "4":  # Seller Name
            item_list=[]
            items = Item.query.all()
            for item in items:
                if search_query.lower() in item.seller.lower():
                    print("matched item ",item)
                    item_list.append(item)

            
            return render_template('search_results.html',my_orders=my_orders,customer=customer,search_results=item_list,is_Category='False')
        elif search_by == "5":  # Manufacture Date
            item_list=[]
            items = Item.query.all()
            for item in items:
                if search_query.lower() in item.manufacture_date.lower():
                    print("matched item ",item)
                    item_list.append(item)

            
            return render_template('search_results.html',my_orders=my_orders,customer=customer,search_results=item_list,is_Category='False')
        else:
            return redirect( url_for('customer_dashboard'))

    else:
        return redirect( url_for('customer_dashboard'))
    



@app.route('/cancel_order/<int:order_id>',methods=['GET'])
def cancel_order(order_id):
    existing_order = Orders.query.filter_by(item_id=order_id).first()
    original_item=Item.query.filter_by(id=existing_order.item_id).first()
    original_item.quantity=original_item.quantity+existing_order.quantity
    
    db.session.delete(existing_order)
    db.session.commit()
    
    return redirect(url_for('customer_dashboard'))
