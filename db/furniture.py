from db.db import Connect
from datetime import datetime, date, timedelta

cur = Connect().getCursor()


class Furniture:
    #return all categories
    def getcategory(self):
        cur.execute("select * from category")
        dbcategory = cur.fetchall()
        return dbcategory

    #return all furnitures
    def getallfurniture(self):
        cur.execute("select * from furniture")
        dbcategory = cur.fetchall()
        return dbcategory

    #return furnitures based on a specific category id
    def getFurByCategory(self, categoryid):
        cur.execute("select * from furniture where categoryid = %s and is_active = true and status = 'on sale'",
                    (categoryid,))
        dbfurniture = cur.fetchall()
        return dbfurniture

    #return a furniture by given id
    def getfurnitureById(self, id):
        cur.execute("select * from furniture where furnitureid = %s", (id,))
        dbfurniture = cur.fetchone()
        return dbfurniture

    #return a furniture by furniture name
    def getfurniture(self, furniturename):
        cur.execute("select * from furniture where furniturename = %s", (furniturename,))
        dbfurniture = cur.fetchone()
        return dbfurniture

    #search and return furnitures by given keyword
    def getfurnituresearch(self, furniturename):
        cur.execute("select * from furniture where furniturename like '%{furniturename}%'")
        dbfurniture = cur.fetchone()
        return dbfurniture

    #return furnitures in shopping cart
    def getFurInCart(self, customerid):
        cur.execute("select * from shoppingcart left join furniture f on shoppingcart.furnitureid = f.furnitureid \
                where shoppingcart.customerid = %s", (customerid,))
        dbfurniturelist = cur.fetchall()
        return dbfurniturelist

    #return a specific furnitrue in customer's shopping cart
    def judgeFurnitureInCart(self, furnitureid, customerid):
        cur.execute("select * from shoppingcart where furnitureid = %s and customerid = %s", (furnitureid, customerid))
        data = cur.fetchone()
        return data

    #add furniture into customer's shopping cart
    def addCart(self, furnitureid, customerid):
        furniture = self.getfurnitureById(furnitureid)
        cur.execute("insert into shoppingcart (furnitureid, customerid, quantity, totalamount) value (%s,%s,%s,%s)",
                    (furnitureid, customerid, 1, furniture.get('sellprice')))

    #remove furniture from customer's shopping cart
    def deleteCart(self, furnitureid, customerid):
        cur.execute("delete from shoppingcart where customerid=%s and furnitureid=%s", (customerid, furnitureid))

    #delete an order from a customer, then change the relevant funiture's status to 'on sale'
    def deleteOrder(self, orderid):
        cur.execute("select furnitureid from `order` where orderid = %s", (orderid,))
        dbfurnitureid = cur.fetchone()
        cur.execute("update furniture set is_active = true, status = 'on sale' where furnitureid = %s",
                    (dbfurnitureid.get('furnitureid'),))
        cur.execute("delete from `order` where orderid = %s", (orderid,))

    #calculate and return the total amount in customer's shopping cart
    def gettotalAmount(self, customerid):
        cur.execute("select totalamount from shoppingcart where customerid=%s", (customerid,))
        dbamount = cur.fetchall()
        total = 0
        if len(dbamount):
            for item in dbamount:
                total += item.get('totalamount')
        return total

    #place an order for a customer, and change the furniture status to 'sold'
    def addOrderAndRelevant(self, customerid, furnitureid, price, address):
        today = date.today()
        enddate = today + timedelta(days=3)
        cur.execute(
            "insert into `order` (customerid, deliverystatus, estimatedarrivaltime, deliveryaddress, orderdate, furnitureid, price) values (%s,%s,%s,%s,%s,%s,%s)",
            (customerid, 'processing', enddate, address, today, furnitureid, price))
        cur.execute("update furniture set is_active = false, status = 'sold' where furnitureid = %s", (furnitureid,))
        self.deleteCart(furnitureid, customerid)

    #return all orders by a period of date
    def getorderbydate(self, startdate, enddate):
        cur.execute("SELECT *, f.furniturename FROM `order` left join furniture as f on `order`.furnitureid = f.furnitureid \
        where orderdate between %s and %s", (startdate,enddate,))
        dborderlist = cur.fetchall()
        return dborderlist
        
    #calculate and return the price summary by a period of date
    def getorderbydatetotal(self, startdate, enddate):
        cur.execute("SELECT coalesce(sum(price),0) as totalcost FROM `order`\
        where orderdate between %s and %s", (startdate,enddate,))
        dborderlist = cur.fetchall()
        return dborderlist

    #return all funitures that brought from customers by a period of date
    def getsalesbydate(self, startdate, enddate):
        cur.execute("select * from furniture where purchasestatus = 'accept' and purchaseddate between %s and %s", (startdate,enddate,))
        dborderlist = cur.fetchall()
        return dborderlist

    #calculate and return the price summary that brought from customers by a period of date
    def getsalesbydatetotal(self, startdate, enddate):
        cur.execute("select coalesce(sum(purchasedprice),0) as totalcost from furniture \
            where purchasestatus = 'accept' and purchaseddate between %s and %s", (startdate,enddate,))
        dborderlist = cur.fetchall()
        return dborderlist
    
    #calculate the Profit or Loss by a period of date
    def getoveralltotal(self, startdate, enddate):
        cur.execute("select coalesce(sum((SELECT coalesce(sum(price),0) as cost FROM `order`\
        where orderdate between %s and %s) - (select coalesce(sum(purchasedprice),0) as total from furniture \
            where purchasestatus = 'accept' and purchaseddate between %s and %s)),0) as totalcost", \
                 (startdate,enddate,startdate,enddate,))
        dborderlist = cur.fetchall()
        return dborderlist  
    
    #get furnitures that having discount by a date
    def getallDiscountfurniture(self, today):
        cur.execute("select * from furniture where discount != 0 and periodofdiscount >= %s",(today,))
        dbdis = cur.fetchall()
        return dbdis

    #return the best seller furnitures
    def getbestsellerfurniture(self):
        cur.execute("select * from furniture where status = 'sold'")
        dbdis = cur.fetchall()
        return dbdis

    #return all reviews
    def review(self):
        cur.execute("select r.customerid, r.description, r.rating, c.firstName from review as r\
        left join customer as c \
        on r.customerid = c.customerid")
        dbrev = cur.fetchall()
        return dbrev