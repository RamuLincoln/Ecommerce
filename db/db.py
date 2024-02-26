import mysql
import connect
import mysql.connector

dbconn = None
connection = None


class Connect:
    #return the cursor object
    def getCursor(self):
        global dbconn
        global connection
        if dbconn is None:
            connection = mysql.connector.connect(user=connect.dbuser,
                                                 password=connect.dbpass, host=connect.dbhost,
                                                 database=connect.dbname, autocommit=True, buffered=True)
            dbconn = connection.cursor(dictionary=True)
            return dbconn
        else:
            return dbconn
