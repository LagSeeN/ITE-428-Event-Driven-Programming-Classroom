import sqlite3


def addData(db, myParam):
    with (sqlite3.connect(db)) as conn:
        conn.row_factory = sqlite3.Row
        sql_commad = '''INSERT INTO Customers ("CustomerID", "CompanyName", "ContactName", "ContactTitle", "Address", "City", "Region", "PostalCode", "Country", "Phone", "Fax") 
                        VALUES (?,?,?,?,?,?,?,?,?,?,?);'''
        conn.execute(sql_commad, myParam)
        conn.commit()


if __name__ == '__main__':
    database = './MyData/Sqlite_Northwind.sqlite3'
    comname = input('ป้อนชื่อบริษัทที่ต้องการ : ')
    contname = input('ป้อนชื่อผู้ติดต่อ : ')
    conttitle = input('ป้อนตำแหน่งผู้ติดต่อ : ')
    address = input('ป้อนที่อยู่ : ')
    city = input('ป้อนเมือง : ')
    region = input('ป้อนเขต : ')
    postcode = input('ป้อนรหัสไปรษณีย์ : ')
    country = input('ป้อนประเทศ : ')
    phone = input('ป้อนชเบอร์โทร : ')
    fax = input('ป้อน fax : ')
    p = [comname[0:5].upper(), comname, contname, conttitle, address, city, region, postcode, country, phone, fax]
    addData(database, p)
