import pymongo


def insertOne():
    with (pymongo.MongoClient('localhost', 27017)) as conn:
        db = conn.get_database('tni_new')
        currID = db.students.insert_one({'id': '5412514', 'name': 'Wichai'})
        print("New record _id = {}".format(currID.inserted_id))


def insertMany():
    with (pymongo.MongoClient('localhost', 27017)) as conn:
        db = conn.get_database('tni_new')
        data = [{'id': '0001', 'name': 'Wichai'}, {'id': '0002', 'name': 'Wichai'}]
        currID = db.students.insert_many(data)
        print("New record _id = {}".format(currID.inserted_ids))


if __name__ == '__main__':
    # insertOne()
    insertMany()
