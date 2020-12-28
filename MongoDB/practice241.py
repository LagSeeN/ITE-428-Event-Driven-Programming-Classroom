import pymongo


def insertMany(productList):
    with (pymongo.MongoClient('localhost', 27017)) as conn:
        db = conn.get_database('tni_new')
        currID = db.products.insert_many(productList)
        print("New record _id = {}".format(currID.inserted_ids))


if __name__ == '__main__':
    inputNum = int(input('Enter Number of New Product : '))

    productList = []
    for i in range(inputNum):
        print('product Number [{}]'.format(i + 1))
        print('=' * 50)
        productname = input('Enter product name   : ')
        price = float(input('Enter product price  : '))
        stock = int(input('Enter product stock  : '))
        productList.append({'key': productname, 'price': price, 'stock': stock})
        print()
    insertMany(productList)
