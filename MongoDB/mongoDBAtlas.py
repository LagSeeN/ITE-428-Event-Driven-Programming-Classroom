import csv
from datetime import datetime

import pymongo


def testCloud():
    # with (pymongo.MongoClient('localhost', 27017)) as conn:
    connectMongoDB = 'mongodb+srv://mongoTNI:Mortician9-Captive-Submitter-Showman@clustertni.kt6oq.mongodb.net/<dbname>?retryWrites=true&w=majority'
    with pymongo.MongoClient(connectMongoDB) as conn:
        db = conn.get_database('sample_airbnb')
        found = db.listingsAndReviews.count_documents({})
        print('Data in {}'.format(found))


def insertMyData():
    connectMongoDB = 'mongodb+srv://adisak:RPGnqPNGypIy6bQJ@cluster0.ffnxq.mongodb.net/<dbname>?retryWrites=true&w=majority'
    with pymongo.MongoClient(connectMongoDB) as conn:
        db = conn.get_database('TNI')
        db.students.insert_one({'id': '60121053-7', 'name': 'Danupol', 'lastname': 'Intranurux',
                                'physical_data': {'weight': 87, 'height': 190}, 'major': 'IT', 'year': 4, 'gpax': 3.50,
                                'updated': datetime.now()})


def BMI():
    connectMongoDB = 'mongodb+srv://adisak:RPGnqPNGypIy6bQJ@cluster0.ffnxq.mongodb.net/<dbname>?retryWrites=true&w=majority'
    with pymongo.MongoClient(connectMongoDB) as conn:
        db = conn.get_database('TNI')
        cursor = db.students.find({})
        for i in cursor:
            print('{} {} (BMI={:.2f})'.format(i['name'], i['lastname'], i['physical_data']['weight'] / (
                    (i['physical_data']['height'] / 100) ** 2)))


def export_student():
    connectMongoDB = 'mongodb+srv://adisak:RPGnqPNGypIy6bQJ@cluster0.ffnxq.mongodb.net/<dbname>?retryWrites=true&w=majority'
    with pymongo.MongoClient(connectMongoDB) as conn:
        db = conn.get_database('TNI')
        cursor = db.students.find({})
        studenlist = []
        for i in cursor:
            bmi = '{:.2f}'.format(i['physical_data']['weight'] / ((i['physical_data']['height'] / 100) ** 2))
            studenlist.append([i['id'], i['name'], i['lastname'], i['gpax'],
                               bmi])
        with open('./MyTextFile/student_data.csv', mode='a', encoding='utf-8', newline='') as fn:
            fw = csv.writer(fn, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
            fw.writerow(['ID','NAME','LASTNAME','GPAX','BMI'])
            fw.writerows(studenlist)


if __name__ == '__main__':
    export_student()
