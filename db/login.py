from db.db import Connect

cur = Connect().getCursor()


class Login:
    #retrieve a customer which is active by given gmail
    def getCustomer(self, data):
        cur.execute(
            f"SELECT * from customer WHERE CONCAT(email) LIKE '{data.get('email')}' and is_active = 1")
        dbcustomer = cur.fetchone()
        return dbcustomer
    
    #retrieve a staff by given gmail
    def getStaff(self, data):
        cur.execute(
            f"SELECT * from staff WHERE CONCAT(email) LIKE '{data.get('email')}'")
        dbstaff = cur.fetchone()
        return dbstaff

