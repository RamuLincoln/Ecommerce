from datetime import date, datetime
import os
from flask import *
from db.db import Connect
from db.login import Login
from db.register import Register
from db.furniture import Furniture
from db.category import Category
import uuid

app = Flask(__name__)
app.secret_key = '123456'

UPLOAD_FOLDER = 'static/images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


cur = Connect().getCursor()

# This is the homepage
@app.route('/')
@app.route('/home')
def home():
    category = Furniture().getcategory()
    today = datetime.today()
    Deals = Furniture().getallDiscountfurniture(today)
    best = Furniture().getbestsellerfurniture()
    review = Furniture().review()
    return render_template("home.html", category=category, Deals=Deals, today=today, best=best,review = review)

#The admin dashboard
@app.route('/admin')
def admin():
    return render_template("admin.html")

#The staff dashboard
@app.route('/staff')
def staff():
    return render_template("staff.html")

#view the details of the furniture
@app.route('/products/<furnitureid>', methods=['GET', 'POST'])
def products(furnitureid):
    customername = session.get('firstname')
    sql = """
    SELECT * FROM furniture
    where furnitureid = %s
    """
    cur.execute(sql, (furnitureid,))
    userDetail = cur.fetchone()
    return render_template("products.html", details=userDetail, customername=customername)

#The customer dashboard
@app.route('/customer')
def customer():
    customername = session.get('firstname')
    category = Furniture().getcategory()
    return render_template("customer.html", category=category, customername=customername)

#Login function
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        data = request.form.to_dict()
        dbcustomer = Login().getCustomer(data)
        dbstaff = Login().getStaff(data)

        # member login
        if dbcustomer is not None:
            session['customerID'] = dbcustomer.get('customerid')
            session['firstname'] = dbcustomer.get('firstname')
            return redirect("/customer")

        # trainer login
        if dbstaff is not None:
            session['staffID'] = dbstaff.get('staffid')
            return redirect("/staff")

        # admin login
        elif data.get('email') == 'admin@gmail.com':
            return redirect("/admin")

        else:
            return render_template("login.html")

#Logout function
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

#This method is for new customer to register
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    else:
        updatedata = request.form.to_dict()
        Register().customerRegister(updatedata)
        customerId = cur.lastrowid
        session['customerID'] = customerId
        session['firstname'] = updatedata.get('firstName')
        return redirect("/customer")

#This method is for admin to add the new customer
@app.route('/addcustomer', methods=['GET', 'POST'])
def addcustomer():
    if request.method == 'GET':
        return render_template("addcustomer.html")
    else:
        updatedata = request.form.to_dict()
        Register().customerRegister(updatedata)
        customerId = cur.lastrowid
        session['customerID'] = customerId
        return redirect("/manageuser")

#Display the shopping cart
@app.route('/shopping_cart', methods=['GET', 'POST'])
def shoppingCart():
    customerid = session.get('customerID')
    customername = session.get('firstname')
    flashmessage = request.args.get('flashmessage')
    if request.method == 'GET':
        dbfurniturelist = Furniture().getFurInCart(customerid)
        today = datetime.today()
    return render_template("cart.html", furniture=dbfurniturelist, flashmessage=flashmessage, customername=customername,
                           today=today)

#For customer to add the product to the shopping cart
@app.route('/add_cart')
def addCart():
    msg = 'Already in cart'
    furnitureid = request.args.get('furnitureid')
    customerid = session.get('customerID')
    data = Furniture().judgeFurnitureInCart(furnitureid, customerid)
    if data is None:
        Furniture().addCart(furnitureid, customerid)
        msg = 'Add cart success'
    return redirect('/shopping_cart?' + 'flashmessage=' + msg)

#For customer to delete the product from the shopping cart
@app.route('/delete_cart')
def deleteCart():
    customerid = session.get('customerID')
    furnitureid = request.args.get('furnitureid')
    Furniture().deleteCart(furnitureid, customerid)
    return redirect('/shopping_cart')

#This method is for customer to delete the order
@app.route('/delete_order')
def deleteOrder():
    orderid = request.args.get('orderid')
    Furniture().deleteOrder(orderid)
    return redirect('/order')

#Customer shopping page
@app.route('/shopping')
def shopping():
    customername = session.get('firstname')
    category = Furniture().getcategory()
    review = Furniture().review()
    return render_template("shopping.html", category=category, review = review, customername=customername)

#Display checkout information
@app.route('/payment', methods=['POST'])
def payment():
    customerid = session.get('customerID')
    customername = session.get('firstname')
    furnitureList = request.form.getlist('furniture')
    totalprice = request.form.get('totalPrice')
    cur.execute("select * from customer where customerid=%s", (customerid,))
    dbcustomer = cur.fetchone()
    if len(furnitureList):
        format_strings = ','.join(['%s'] * len(furnitureList))
        cur.execute("select * from furniture where furnitureId in (%s)" % format_strings, tuple(furnitureList))
        furnitureList = cur.fetchall()
        today = datetime.today()
        return render_template("payment.html", customer=dbcustomer, furnitureList=furnitureList,
                               customername=customername,
                               totalprice=totalprice, today=today)
    else:
        return redirect('/shopping_cart')

#Process checkout
@app.route('/check_out', methods=['POST'])
def addOrder():
    customerid = session.get('customerID')
    furnitureList = request.form.getlist('furnitureList')
    priceList = request.form.getlist('sellprice')
    address = request.form.to_dict().get('address')
    for i, furnitureid in enumerate(furnitureList):
        Furniture().addOrderAndRelevant(customerid, furnitureid, priceList[i], address)
    return redirect('/order')

#Display specific customer's order list
@app.route('/order', methods=['GET', 'POST'])
def getorder():
    customerid = session.get('customerID')
    customername = session.get('firstname')
    if request.method == 'GET':
        cur.execute(
            "select * from `order` left join furniture on `order`.furnitureid = furniture.furnitureid where "
            "`order`.customerid = %s",
            (customerid,))
        dborder = cur.fetchall()
        return render_template("order.html", order=dborder, customername=customername)

#The request function for customer
@app.route('/request', methods=['GET', 'POST'])
def getRequest():
    customerid = session.get('customerID')
    customername = session.get('firstname')
    if request.method == 'GET':
        cur.execute("select * from requests where customerid = %s", (customerid,))
        dbrequest = cur.fetchall()
        return render_template("request.html", customername=customername, requests=dbrequest)
    else:
        data = request.form.to_dict()
        today = date.today()
        cur.execute("insert into requests (customerid, description, category, furniturename, requestdate) values \
        (%s,%s,%s,%s,%s)",
                    (customerid, data.get('description'), data.get('category'), data.get('furniturename'), today))
        return redirect('/request')

#The function for staff to view customer's requests
@app.route('/staff_response', methods=['GET', 'POST'])
def staffResponse():
    cur.execute("select * from requests left join customer on requests. customerid = customer.customerid \
                    where customer.is_active = 1")
    dbrequest = cur.fetchall()
    return render_template("staff_response_customer.html", requests=dbrequest)

#The function for staff to view request detail and response customer's requests
@app.route('/view_request', methods=['GET', 'POST'])
def getStaffResponse():
    if request.method == 'GET':
        requestid = request.args.get('requestid')
        cur.execute("select * from requests where id = %s", (requestid,))
        dbrequest = cur.fetchone()
        response = dbrequest.get('response')
        return render_template("staff_view_request.html", request=dbrequest, response=response, id=requestid)
    else:
        response = request.form.to_dict()
        today = date.today()
        cur.execute("update requests set response=%s, reponsedate=%s where id=%s",
                    (response.get('reply'), today, response.get('id')))
        return redirect('/staff_response')

#List furnitures based on specific category 
@app.route('/fur')
def fur():
    categoryid = request.args.get('categoryid')
    dbfurniture = Furniture().getFurByCategory(categoryid)
    customername = session.get('firstname')
    today = datetime.today()
    return render_template("furniture.html", furniture=dbfurniture, categoryid=categoryid, customername=customername,
                           today=today)

#Search funitures by given key word 
@app.route('/search', methods=['GET', 'POST'])
def search():
    today = datetime.today()
    if request.method == 'POST':
        searchval = request.form['search']
        cur.execute(f"""Select * from furniture 
                        WHERE furniturename LIKE '%{searchval}%' and is_active = True""")
        Furnituren = cur.fetchall()
        if Furnituren is None:
            flash("Searched product not available at the moment. Please check after sometime")
            category = Furniture().getcategory()
            customername = session.get('firstname')
            return render_template("home.html", category=category, customername=customername)

        return render_template("searchproducts.html", furniture=Furnituren, today=today)

#For admin to view all of the furnitures
@app.route('/managefur')
def managefur():
    cur.execute("select f.furnitureid, f.image, f.furniturename, f.periodofdiscount, f.description, f.purchasedprice,f.sellprice, \
        f.discount, f.status,\
        r.cost as refurbishedprice, c.firstname as sellerinfo\
        from furniture as f\
        left join refurbishment as r\
        on f.refurbishid = r.refurbishid\
        left join customer as c\
        on f.customerid = c.customerid\
        where f.is_active = 1\
        union\
        \
select f.furnitureid, f.image, f.furniturename, f.periodofdiscount, f.description, f.purchasedprice,f.sellprice, f.discount, f.status,\
        r.cost as refurbishedprice, c.firstname as sellerinfo\
        from furniture as f\
        left join refurbishment as r\
        on f.refurbishid = r.refurbishid\
        left join seller as c\
        on f.sellerid = c.sellerid \
        where f.is_active = 1;")
    dbfurniture = cur.fetchall()
    return render_template("managefurniture.html", furniture=dbfurniture)

#For admin to view all of the users
@app.route('/manageuser')
def manageuser():
    cur.execute("select * from customer where is_active = 1;")
    dbuser = cur.fetchall()
    return render_template("manageuser.html", user=dbuser)

#For admin to view all of the staffs
@app.route('/managestaff')
def managestaff():
    cur.execute("select * from staff where is_active = 1;")
    dbstaff = cur.fetchall()
    return render_template("managestaff.html", staff=dbstaff)

#List furnitures for staff to manage
@app.route('/staffmanagefur')
def staffmanagefur():
    cur.execute("select f.furnitureid, f.image, f.furniturename, f.periodofdiscount, f.description, f.purchasedprice,f.sellprice, f.discount, f.status,\
        r.cost as refurbishedprice, c.firstname as sellerinfo\
        from furniture as f\
        left join refurbishment as r\
        on f.refurbishid = r.refurbishid\
        left join customer as c\
        on f.customerid = c.customerid \
        where f.is_active = 1;")
    dbfurniture = cur.fetchall()
    return render_template("staffmanagefurniture.html", furniture=dbfurniture)

#For Staff to view the furniture details
@app.route('/staffviewfurniture/<furnitureid>', methods=['GET', 'POST'])
def staffViewFur(furnitureid):
    sql = """
    select * from furniture left join refurbishment on furniture.refurbishid = refurbishment.refurbishid left join seller as s \
    on furniture.sellerid = s.sellerid \
    where furnitureid=%s;
    """
    cur.execute(sql, (furnitureid,))
    staffFur = cur.fetchone()
    return render_template("staffFurnitureView.html", details=staffFur)

#Staff update the furniture details
@app.route('/staffviewfurnitureUpdate', methods=['GET', 'POST'])
def StaffviewfurnitureUpdate():
    if request.method == 'POST':
        description = request.form.get('description')
        salePrice = request.form.get('sellprice')
        furnitureid = request.form.get('furnitureid')
        refurbishedPrice = request.form.get('refurbishedprice')
        purchasedprice = request.form.get('purchasedprice')
        discount = request.form.get('discount')
        discountdate = request.form.get('periodofdiscount')
        image = request.files['sel_Photo']

        app_route = os.path.dirname(os.path.abspath(__file__))
        target = os.path.join(app_route, 'static/images/')
        new_file_name = str(uuid.uuid4()) + '.' + image.filename.split('.')[1]
        destination = "/".join([target, new_file_name])
        image.save(destination)
        image_loc = "/static/images/" + new_file_name

        sql = (
            "update furniture set description = %s, sellprice = %s,  purchasedprice = %s, discount = %s, "
            "periodofdiscount = %s, image=%s  where furnitureid = %s")
        result = cur.execute(sql, (
            description, salePrice, purchasedprice, discount, discountdate, image_loc, furnitureid))
        sql = (
            "update refurbishment set cost = %s where refurbishid = %s")
        cur.execute(sql, (refurbishedPrice, furnitureid))
        return redirect(url_for("staffmanagefur", furniture=result))
    else:
        return redirect(url_for("staffmanagefur"))

#For admin to view the furniture details
@app.route('/viewfur/<furnitureid>', methods=['GET', 'POST'])
def viewFurnitureDetail(furnitureid):
    sql = """
    select * from furniture left join refurbishment on furniture.refurbishid = refurbishment.refurbishid left join seller as s \
    on furniture.sellerid = s.sellerid \
    where furnitureid=%s;
    """
    cur.execute(sql, (furnitureid,))
    userDetail = cur.fetchone()
    return render_template("furnitureView.html", details=userDetail)

#For admin to update the furniture details
@app.route('/viewfurnitureUpdate', methods=['GET', 'POST'])
def viewfurnitureUpdate():
    if request.method == 'POST':
        categoryId = request.form.get('categoryid')
        saleStatus = request.form.get('status')
        activeStatus = request.form.get('is_active')
        description = request.form.get('description')
        salePrice = request.form.get('sellprice')
        furnitureid = request.form.get('furnitureid')
        refurbishedPrice = request.form.get('refurbishedprice')
        purchasedprice = request.form.get('purchasedprice')
        sql = (
            "update furniture set categoryid = %s, status = %s, is_active = %s, description = %s, sellprice = %s,  "
            "purchasedprice = %s  where furnitureid = %s")
        result = cur.execute(sql, (
            categoryId, saleStatus, activeStatus, description, salePrice, purchasedprice, furnitureid))
        sql = (
            "update refurbishment set cost = %s where refurbishid = %s")
        cur.execute(sql, (refurbishedPrice, furnitureid))
        return redirect(url_for("managefur", furniture=result))
    else:
        return redirect(url_for("managefur"))


#For admin to update the furniture details
@app.route('/staffaddfurniture', methods=['GET', 'POST'])
def staffaddfurniture():
    if request.method == 'POST':
        furniturename = request.form.get('furniturename')
        activeStatus = 1
        description = request.form.get('description')
        salePrice = request.form.get('sellprice')
        purchasedprice = request.form.get('purchasedprice')
        sellerid = request.form.get('Sellerid')

        cur.execute("insert into furniture (furniturename,is_active,description,sellprice,purchasedprice,sellerid) values \
                (%s,%s,%s,%s,%s,%s)",(furniturename, 1, description, salePrice, purchasedprice,sellerid, ))
        return redirect(url_for("staffmanagefur"))
    else:
        return render_template("staffaddfur.html")

#For admin to view customer details
@app.route('/viewuser/<customerid>', methods=['GET', 'POST'])
def viewUserDetail(customerid):
    sql = """
    SELECT * FROM customer
    where customerid = %s
    """
    cur.execute(sql, (customerid,))
    userDetail = cur.fetchone()
    return render_template("manageuserview.html", details=userDetail)

#For admin to update customer's phone number and address
@app.route('/viewUserUpdate', methods=['GET', 'POST'])
def viewuserUpdate():
    if request.method == 'POST':
        phone = request.form.get('phone')
        address = request.form.get('address')
        customerid = request.form.get('customerid')
        sql = "update customer set phone = %s, address = %s where customerid = %s"
        result = cur.execute(sql, (phone, address, customerid))
        return redirect(url_for("manageuser", user=result))
    else:
        return redirect(url_for("manageuser"))

#For admin to view staff detail
@app.route('/viewstaff/<staffid>', methods=['GET', 'POST'])
def viewStaffDetail(staffid):
    sql = """
    SELECT * FROM staff
    where staffid = %s
    """
    cur.execute(sql, (staffid,))
    userDetail = cur.fetchone()
    return render_template("managestaffview.html", details=userDetail)

#For admin to update staff's address
@app.route('/viewStaffUpdate', methods=['GET', 'POST'])
def viewstaffUpdate():
    if request.method == 'POST':
        address = request.form.get('address')
        staffid = request.form.get('staffid')
        sql = "update staff set address = %s where staffid = %s"
        result = cur.execute(sql, (address, staffid))
        return redirect(url_for("managestaff", staff=result))
    else:
        return redirect(url_for("managestaff"))

#For admin to delete the furniture
#Only make specific furniture inactive
@app.route('/delFur/<furnitureid>', methods=['GET', 'POST'])
def delFurniture(furnitureid):
    if request.method == 'POST':
        furnitureid = request.form.get('furnitureid')
        sql = """
        update furniture set is_active= 0
        where furnitureid=%s
        """
        cur.execute(sql, (furnitureid,))
        flash('Successfully made the furniture Inactive')
        return redirect(url_for('managefur'))
    else:
        return render_template("furniture_delete.html", furniture_id=furnitureid)

#For admin to delete the customer
#Only make specific CUSTOMER inactive
@app.route('/deluser/<customerid>', methods=['GET', 'POST'])
def delUser(customerid):
    if request.method == 'POST':
        customerid = request.form.get('customerid')
        sql = """
        update customer set is_active= 0
        where customerid=%s
        """
        cur.execute(sql, (customerid,))
        flash('Successfully made the customer Inactive')
        return redirect(url_for('manageuser'))
    else:
        btn_disable = ""
        sql = """
        select count(*) not_comp_amt
        from furniture.order 
        where customerid = %s
        and deliverystatus != 'delivered'
        """
        cur.execute(sql, (customerid,))
        dbRst = cur.fetchone()

        if dbRst.get('not_comp_amt') == 0:
            title_msg = "Are you sure to delete this User?"
        else:
            title_msg = "Sorry, this account can't be deleted. Still have orders not completed yet."
            btn_disable = "disabled"

        return render_template("user_delete.html", customerid=customerid, title_msg=title_msg, btn_disable=btn_disable)

#For admin to delete the staff
#Only make specific staff inactive
@app.route('/delstaff/<staffid>', methods=['GET', 'POST'])
def delstaff(staffid):
    if request.method == 'POST':
        staffid = request.form.get('staffid')
        sql = """
        update staff set is_active= 0
        where staffid=%s
        """
        cur.execute(sql, (staffid,))
        flash('Successfully made the staff Inactive')
        return redirect(url_for('managestaff'))
    else:
        return render_template("staff_delete.html", staffid=staffid)

#Staff receives furniture that customers are selling
@app.route('/staffresponse')
def staffresponse():
    cur.execute("""select f.furnitureid,f.image,f.furniturename,f.description,f.purchasedprice,f.purchasestatus,c.firstname
        from furniture as f
        left join customer as c
        on f.customerid = c.customerid
        where f.is_active = 0 and f.status is null;""")
    dbfurniture = cur.fetchall()
    return render_template("staffresponse.html", furniture=dbfurniture)

#Staff accept customers selling furniture
@app.route('/staffaccept/<furnitureid>', methods=['GET', 'POST'])
def customerSellFur(furnitureid):
    sql = ("select f.furnitureid, f.image, f.furniturename, f.description, f.purchasedprice from furniture as f \
        where f.furnitureid = %s")

    cur.execute(sql, (furnitureid,))
    userDetail = cur.fetchone()
    today = date.today()
    return render_template("staff_accept.html", details=userDetail, today=today)

#Staff update furniture information that were purchased from the customers
@app.route('/staffAcceptUpdate', methods=['GET', 'POST'])
def staffAcceptUpdate():
    if request.method == 'POST':
        furnitureid = request.form.get('furnitureid')
        status = request.form.get('status')
        funitureName = request.form.get('furniturename')
        description = request.form.get('description')
        purchased = request.form.get('purchasedprice')
        sellPrice = request.form.get('sellprice')
        purchasedDate = request.form.get('purchaseddate')
        refurbishid = furnitureid
        staffid = 1
        active = 2
        cur.execute("INSERT INTO `refurbishment` VALUES (%s,null,null,null,null)", (refurbishid,))
        sql = (
            "update furniture set furniturename = %s, description = %s, purchasedprice = %s, staffid = %s, "
            "refurbishid = %s, purchaseddate = %s, purchasestatus = %s, is_active = %s where furnitureid = %s")
        result = cur.execute(sql, (
            funitureName, description, purchased, staffid, refurbishid, purchasedDate, status, active, furnitureid))
        return redirect(url_for('staffresponse', fur=result))
    else:
        return redirect(url_for('staffresponse'))

#Staff accept customers selling furniture
@app.route('/staffreject/<furnitureid>', methods=['GET', 'POST'])
def staffreject(furnitureid):
    sql = ("select f.furnitureid, f.image, f.furniturename, f.description, f.purchasedprice from furniture as f \
        where f.furnitureid = %s")

    cur.execute(sql, (furnitureid,))
    userDetail = cur.fetchone()
    return render_template("staff_reject.html", details=userDetail)

#Staff update furniture information that were purchased from the customers
@app.route('/staffrejectUpdate', methods=['GET', 'POST'])
def staffrejectUpdate():
    if request.method == 'POST':
        furnitureid = request.form.get('furnitureid')
        status = request.form.get('status')
        active = 2
        sql = ("update furniture set purchasestatus = %s, is_active = %s where furnitureid = %s")
        result = cur.execute(sql, (status, active, furnitureid))
        return redirect(url_for('staffresponse', fur=result))
    else:
        return redirect(url_for('staffresponse'))

#Staff accept customers selling furniture
@app.route('/stafftrack', methods=['GET', 'POST'])
def stafftrack():
    cur.execute("select f.furnitureid, f.image, f.furniturename, f.description, f.purchasedprice, f.sellprice,\
        f.discount, f.status, r.cost as refurbishedcost, \
        s.firstname as seller\
        from furniture as f\
        left join refurbishment as r\
        on f.refurbishid = r.refurbishid\
        left join customer as s\
        on f.customerid = s.customerid \
        where f.is_active = 2 and f.purchasestatus = 'accept';")

    userDetail = cur.fetchall()
    return render_template("stafftrack.html", furniture=userDetail)

#Staff view furniture's refurbish status
@app.route('/staffviewfur/<furnitureid>', methods=['GET', 'POST'])
def staffviewFur(furnitureid):
    sql = """
    select * from furniture left join refurbishment on furniture.refurbishid = refurbishment.refurbishid left join seller as s \
    on furniture.sellerid = s.sellerid \
    where furnitureid=%s;
    """
    cur.execute(sql, (furnitureid,))
    userDetail = cur.fetchone()
    return render_template("stafftrackstatus.html", details=userDetail)

#Staff update furniture's refurbish
@app.route('/stafffurnitureUpdate', methods=['GET', 'POST'])
def stafffurnitureUpdate():
    if request.method == 'POST':
        saleStatus = request.form.get('status')
        description = request.form.get('description')
        salePrice = request.form.get('sellprice')
        furnitureid = request.form.get('furnitureid')
        refurbishedPrice = request.form.get('refurbishedprice')
        purchasedprice = request.form.get('purchasedprice')
        active = True
        sql = (
            "update furniture set purchasestatus = %s, description = %s, sellprice = %s,  purchasedprice = %s, "
            "is_active = %s where furnitureid = %s")
        result = cur.execute(sql, (
            saleStatus, description, salePrice, purchasedprice, active, furnitureid))
        sql = (
            "update refurbishment set cost = %s where refurbishid = %s")
        cur.execute(sql, (refurbishedPrice, furnitureid))
        return redirect(url_for("stafftrack", furniture=result))
    else:
        return redirect(url_for("staff"))

#Customer track the selling furniture status
@app.route('/customertrackstatus', methods=['GET', 'POST'])
def customertrackstatus():
    customerid = session.get('customerID')
    customername = session.get('firstname')
    cur.execute("select furnitureid, image, furniturename, description, purchasedprice, purchasestatus, bargainPrice\
            from furniture\
            where customerid = %s", (customerid,))
    dbfurniture = cur.fetchall()
    return render_template("customertrackstatus.html", furniture=dbfurniture, customername=customername)

#Admin view the list of category
@app.route('/managecate')
def managecate():
    cur.execute("select * from category where is_active = 1;")
    dbcategory = cur.fetchall()
    return render_template("managecate.html", category=dbcategory)

#Admin delete the category if there is no furnitures in that category
@app.route('/delcategory/<categoryid>', methods=['GET', 'POST'])
def delcategory(categoryid):
    # make specific Category inactive
    if request.method == 'POST':
        categoryid = request.form.get('categoryid')
        sql = """
        update category set is_active= 0
        where categoryid=%s
        """
        cur.execute(sql, (categoryid,))
        flash('Successfully deleted the category')
        return redirect(url_for('managecate'))
    else:
        btn_disable = ""
        sql = """
        select count(*) has_fur
        from furniture.furniture
        where categoryid = %s
        and is_active = 1
        """
        cur.execute(sql, (categoryid,))
        dbRst = cur.fetchone()

        if dbRst.get('has_fur') == 0:
            msg = "Are you sure to delete this Category?"
        else:
            msg = "Sorry, this category can't be deleted. Still have items on it."
            btn_disable = "disabled"
        return render_template("category_delete.html", categoryid=categoryid, msg=msg, btn_disable=btn_disable)

#Admin add new category
@app.route('/addcategory', methods=['GET', 'POST'])
def addcategory():
    if request.method == 'POST':
        categoryname = request.form.get('categoryName')
        description = request.form.get('description')

        objCategory = Category()

        if not objCategory.isCategoryExist(categoryname):
            objCategory.addCategory(categoryname, description)
            return redirect(url_for('managecate'))
        elif objCategory.isInactive(categoryname):
            objCategory.set_active(categoryname)
            return redirect(url_for('managecate'))
        else:
            flash(categoryname + " has already existed in system.")
            return render_template("addcategory.html")
    else:
        return render_template("addcategory.html")

#Admin update the category name and description
@app.route('/updateCate', methods=['GET', 'POST'])
def updatecategory():
    if request.method == 'POST':
        categoryid = request.form.get('categoryid')
        categoryname = request.form.get('categoryname')
        description = request.form.get('description')
        objCategory = Category()
        objCategory.updateCategory(categoryid, categoryname, description)
    return redirect(url_for('managecate'))

#Admin view the category detail
@app.route('/viewCategory/<categoryid>', methods=['GET', 'POST'])
def viewCateDetail(categoryid):
    objCategory = Category()
    cateDetail = objCategory.getCategoryByID(categoryid)
    return render_template("edit_category.html", details=cateDetail)

#Customer review a specific order
@app.route('/customerrev/<orderid>', methods=['GET', 'POST'])
def customerrev(orderid):
    customerid = session.get('customerID')
    cur.execute(
        "select * from `order` left join furniture on `order`.furnitureid = furniture.furnitureid where "
        "`order`.customerid = %s and orderid = %s",
        (customerid, orderid,))
    orderDetail = cur.fetchone()
    return render_template("customerreview.html", details=orderDetail)

#Customer see their feedbacks
@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    customerid = session.get('customerID')
    customername = session.get('firstname')
    cur.execute("select r.description, r.rating, f.furniturename from review as r\
    left join `order` as o\
    on o.orderid = r.orderid\
    left join furniture as f\
    on o.furnitureid = f.furnitureid  where r.customerid = %s", (customerid,))
    dbrequest = cur.fetchall()
    return render_template("feedback.html", customername=customername, requests=dbrequest)

#Customer make reviews on order
@app.route('/customerreview', methods=['GET', 'POST'])
def customerreview():
    orderid = request.form.get('orderid')
    review = request.form.get('review')
    rating = request.form.get('stars')
    customerid = session.get('customerID')
    customername = session.get('firstname')
    if request.method == 'POST':
        cur.execute("insert into review (customerid, orderid, description, rating) values \
            (%s,%s,%s,%s)",
                    (customerid, orderid, review, rating))
        return redirect("/feedback")
    else:
        cur.execute("select * from review where customerid = %s", (customerid,))
        dbrequest = cur.fetchall()
        return render_template("customerreview.html", customername=customername, requests=dbrequest)

#Staff view customer's feedbacks 
@app.route('/stafffeedback', methods=['GET', 'POST'])
def stafffeedback():
    cur.execute("select r.description, r.rating, c.firstname, f.furniturename from review as r\
    left join `order` as o\
    on o.orderid = r.orderid\
    left join furniture as f\
    on o.furnitureid = f.furnitureid \
    left join customer as c\
    on c.customerid = r.customerid")
    dbrequest = cur.fetchall()
    return render_template("feedbackstaff.html", requests=dbrequest)

#Customer sell the second-hand furniture
@app.route('/customersell', methods=['GET', 'POST'])
def uploaded_photo():
    customerid = session.get('customerID')
    customername = session.get('firstname')
    if request.method == 'POST':
        app_route = os.path.dirname(os.path.abspath(__file__))
        target = os.path.join(app_route, 'static/images/')
        name = request.form.get('furniturename')
        image = request.files['selPhoto']
        description = request.form.get('description')
        price = request.form.get('sellprice')
        purchasestatus = "pending"
        active = False
        new_file_name = str(uuid.uuid4()) + '.' + image.filename.split('.')[1]
        destination = "/".join([target, new_file_name])
        image.save(destination)
        image_loc = "/static/images/" + new_file_name

        sql = """
        INSERT INTO `furniture`.`furniture`
        (`furniturename`,`purchasedprice`,`description`,`customerid`, `purchasestatus`,`image`, `is_active`)
        VALUES ( %s,%s,%s,%s,%s,%s,%s);
         """
        cur.execute(sql, (name, price, description, customerid, purchasestatus, image_loc, active))
        flash(" The sell item has been uploaded.")
        return render_template("customersell.html", customername=customername)
    else:
        return render_template("customersell.html", image="", customername=customername)

#Staff bargain the price
@app.route('/staffbargain/<furnitureid>', methods=['GET', 'POST'])
def staffbargain(furnitureid):
    sql = ("select f.furnitureid, f.image, f.furniturename, f.description, f.purchasedprice from furniture as f \
        where f.furnitureid = %s")
    cur.execute(sql, (furnitureid,))
    userDetail = cur.fetchone()
    return render_template("staff_bargain.html", details=userDetail)

#Staff set the bargain price
@app.route('/bargainUpdate', methods=['GET', 'POST'])
def bargainUpdate():
    if request.method == 'POST':
        furnitureid = request.form.get('furnitureid')
        bargainPrice = request.form.get('bargainprice')
        sql = "update furniture set bargainPrice =%s , purchasestatus = 'bargaining' where furnitureid = %s"
        cur.execute(sql, (bargainPrice, furnitureid))
        return redirect(url_for('staffresponse'))

#Customer accept or reject the bargain
@app.route('/customerBargainUpdate', methods=['GET', 'POST'])
def customerBargainUpdate():
    if request.method == 'POST':
        furnitureid = request.form.get('furnitureid')

        if request.form.get('submit_action') == "Accept":
            sql = (
                "update furniture set purchasedPrice = bargainPrice, purchasestatus = 'Customer Accepted' where "
                "furnitureid = %s")
        else:
            sql = "update furniture set purchasestatus = 'Customer Rejected' where furnitureid = %s"

        cur.execute(sql, (furnitureid,))
        return redirect(url_for('customertrackstatus'))

#Admin generate the reports
@app.route('/report', methods=['GET', 'POST'])
def report():
    if request.method == 'POST':
        startdate = request.form.get('startdate')
        enddate = request.form.get('enddate')
        order = Furniture().getorderbydate(startdate, enddate)
        order1 = Furniture().getsalesbydate(startdate, enddate)
        order2 = Furniture().getorderbydatetotal(startdate, enddate)
        order3 = Furniture().getsalesbydatetotal(startdate, enddate)
        order4 = Furniture().getoveralltotal(startdate, enddate)
        return render_template('report.html', order=order, order1=order1, order2=order2, order3=order3, order4=order4,
                               startdate=startdate, enddate=enddate)
    else:
        return render_template('report.html')

#Staff see the list of orders 
@app.route('/orderlist')
def orderlist():
    cur.execute(
        """select b.furniturename,b.image,b.description,a.orderid,a.deliveryaddress,a.orderdate,a.deliverystatus,a.estimatedarrivaltime,a.price
            from furniture.order as a
            left join furniture.furniture as b
            on a.furnitureid = b.furnitureid""")
    orderList = cur.fetchall()
    return render_template("updateOrderStatus.html", orderlist=orderList)

#Staff view the order details
@app.route('/viewOrderDetail/<orderid>', methods=['GET', 'POST'])
def viewOrderDetail(orderid):
    if orderid is not None:
        cur.execute(
            """select b.furniturename,b.image,b.description,a.orderid,a.deliveryaddress,a.orderdate,a.deliverystatus,a.estimatedarrivaltime,a.price
            from furniture.order as a
            left join furniture.furniture as b
            on a.furnitureid = b.furnitureid
            where a.orderid = %s""", (orderid,))

        orderDetail = cur.fetchone()

        return render_template("orderView.html", details=orderDetail)
    else:
        return redirect('/orderlist')

#Staff update the order status 
@app.route('/updateStatus', methods=['GET', 'POST'])
def updateOrderStatus():
    if request.method == 'POST':
        orderid = request.form.get('orderid')
        sel_value = request.form.get('sel_Status')

        cur.execute(
            """update furniture.order
            set deliverystatus = %s
            where orderid = %s""", (sel_value, orderid,))

        return redirect('/orderlist')
    else:
        return redirect('/orderlist')


if __name__ == "__main__":
    app.run(debug=True)
