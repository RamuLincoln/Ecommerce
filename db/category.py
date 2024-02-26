from db.db import Connect
from datetime import datetime, date, timedelta

cur = Connect().getCursor()


class Category:
    #Add the new category
    def addCategory(self, categoryname, description):
        cur.execute("insert into category (categoryname, description) value (%s,%s)", (categoryname, description))

    #update category as inactive
    def set_active(self, categoryname):
        cur.execute("update category set is_active = 1 where categoryname = %s",(categoryname,))

    #check whether the category exist or not
    def isCategoryExist(self, categoryname) -> bool:
        sql = """
        select
            count(*) found_cate_amt
        from category
        where categoryname = %s
        """
        cur.execute(sql, (categoryname,))
        dbRst = cur.fetchone()

        if (dbRst.get('found_cate_amt') == 0):
            return False
        else:
            return True

    #check whether the category active or not
    def isInactive(self, categoryname) -> bool:
        sql = """
        select
            count(*) found_Inactive
        from category
        where categoryname = %s and is_active = 0
        """
        cur.execute(sql, (categoryname,))
        dbRst = cur.fetchone()

        if (dbRst.get('found_Inactive') == 0):
            return False
        else:
            return True

    #update category
    def updateCategory(self, id, categoryname, description):
        cur.execute("update category set categoryname=%s, description=%s where categoryid=%s", (categoryname, description, id))

    #return a category by id
    def getCategoryByID(self, id):
        cur.execute("select * from category where categoryid = %s", (id,))
        return cur.fetchone()