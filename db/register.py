from db.db import Connect

cur = Connect().getCursor()


class Register:
    #register a customer by given data
    def customerRegister(self, data):
        cur.execute("insert into customer (firstName, lastName, DOB, phone, email, address, is_active) values \
                        (%s,%s,%s,%s,%s,%s,%s)",
                    (data.get('firstName'),
                     data.get('lastName'),
                     data.get('DOB'),
                     data.get('phone'),
                     data.get('email'),
                     data.get('address'),
                     1,))

