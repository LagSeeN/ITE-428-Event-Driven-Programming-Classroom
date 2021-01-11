import csv
from datetime import datetime

import pymongo

connectTNIMongoDB = 'mongodb+srv://adisak:RPGnqPNGypIy6bQJ@cluster0.ffnxq.mongodb.net/<dbname>?retryWrites=true&w=majority'
connectMyMongoDB = 'mongodb+srv://mongoTNI:Mortician9-Captive-Submitter-Showman@clustertni.kt6oq.mongodb.net/<dbname>?retryWrites=true&w=majority'


def testCloud():
    # with (pymongo.MongoClient('localhost', 27017)) as conn:
    with pymongo.MongoClient(connectMyMongoDB) as conn:
        db = conn.get_database('sample_airbnb')
        found = db.listingsAndReviews.count_documents({})
        print('Data in {}'.format(found))


def insertMyData():
    with pymongo.MongoClient(connectTNIMongoDB) as conn:
        db = conn.get_database('TNI')
        db.students.insert_one({'id': '60121053-7', 'name': 'Danupol', 'lastname': 'Intranurux',
                                'physical_data': {'weight': 87, 'height': 190}, 'major': 'IT', 'year': 4, 'gpax': 3.50,
                                'updated': datetime.now()})


def BMI():
    with pymongo.MongoClient(connectTNIMongoDB) as conn:
        db = conn.get_database('TNI')
        cursor = db.students.find({})
        for i in cursor:
            print('{} {} (BMI={:.2f})'.format(i['name'], i['lastname'], i['physical_data']['weight'] / (
                    (i['physical_data']['height'] / 100) ** 2)))


def export_student():
    with pymongo.MongoClient(connectTNIMongoDB) as conn:
        db = conn.get_database('TNI')
        cursor = db.students.find({})
        studenlist = []
        for i in cursor:
            bmi = float('{:.2f}'.format(i['physical_data']['weight'] / ((i['physical_data']['height'] / 100) ** 2)))
            studenlist.append([i['id'], i['name'], i['lastname'], i['gpax'],
                               bmi])
        with open('./MyTextFile/student_data.csv', mode='w', encoding='utf-8', newline='') as fn:
            fw = csv.writer(fn, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
            fw.writerow(['ID', 'NAME', 'LASTNAME', 'GPAX', 'BMI'])
            fw.writerows(studenlist)


def import_student():
    student = []
    with open('./MyTextFile/student_data.csv', mode='r', encoding='utf-8', newline='') as fn:
        fr = csv.reader(fn, quoting=csv.QUOTE_NONNUMERIC)
        csv_headings = next(fr)
        for i in fr:
            student.append({csv_headings[0].lower(): i[0],
                            csv_headings[1].lower(): i[1],
                            csv_headings[2].lower(): i[2],
                            csv_headings[3].lower(): i[3],
                            csv_headings[4].lower(): i[4]})
    with pymongo.MongoClient(connectTNIMongoDB) as conn:
        db = conn.get_database('TNI')
        db.danupol.insert_many(student)


def testUpdate():
    with pymongo.MongoClient(connectTNIMongoDB) as conn:
        db = conn.get_database('TNI')
        result = db.danupol.update_one({'id': {'$eq': '11111111'}}, {'$set': {'gpax': 3.8}})
        print('Match : {}\nUpdate : {}'.format(result.matched_count, result.modified_count))


def testUpdateMany():
    with pymongo.MongoClient(connectTNIMongoDB) as conn:
        db = conn.get_database('TNI')
        result = db.narawit.update_many({'gpax': {'$lt': 3}}, {'$set': {'bmi': 50}})
        print('Match : {}\nUpdate : {}'.format(result.matched_count, result.modified_count))


def testRemove():
    with pymongo.MongoClient(connectTNIMongoDB) as conn:
        db = conn.get_database('TNI')
        where = {'bmi': 500}
        result = db.narawit.delete_one(where)
        # result = db.narawit.delete_many(where)
        print("ลบได้ = {}".format(result.delete_count))


def air_bnb():
    with pymongo.MongoClient(connectMyMongoDB) as conn:
        db = conn.get_database('sample_airbnb')
        where = {'$and': [{'cancellation_policy': 'flexible'},
                          {'bedrooms': {'$gt': 3}},
                          {'price': {'$lt': 100}},
                          {'cleaning_fee': {'$exists': 'true'}}]}
        order_by = [('property_type', 1)]
        found = db['listingsAndReviews'].count_documents(where)
        cursor = db['listingsAndReviews'].find(where).sort(order_by)
        print('Found = {}'.format(found))
        count = 1
        for i in cursor:
            print('{}.\nNAME = {}\nTYPE = {}\nCleaning Fee = {}'.format(count, i['name'], i['property_type'],
                                                                        i['cleaning_fee']))
            print('-' * 50)
            count += 1


def cleaning_fee():
    with pymongo.MongoClient(connectMyMongoDB) as conn:
        db = conn.get_database('sample_airbnb')
        where = {'cleaning_fee': {'$exists': 'true'}}
        order_by = [('property_type', 1)]
        found = db['listingsAndReviews'].count_documents(where)
        cursor = db['listingsAndReviews'].find(where).sort(order_by)
        print('Found = {}'.format(found))
        total = 0
        for i in cursor:
            print('Place = {}\nCountry = {}\nCleaning Fee = {}'.format(i['name'], i['address']['country'],
                                                                       i['cleaning_fee']))
            print('-' * 50)
            total += i['cleaning_fee'].to_decimal()
        print('Average = {:.2f}'.format(total / found))


def setNewDataToStudent():
    with pymongo.MongoClient(connectMyMongoDB) as conn:
        db = conn.get_database('TNI')
        where = {'id': '11111111'}
        # setTo = {'$set': {'score': 10}}
        # setTo = {'$set': {'score': {'midterm': 30, 'final': 40}}}
        # setTo = {'$set': {'score': {'midterm': 70}}}
        # setTo = {'$set': {'score.midterm': 70}}
        # setTo = {'$set': {'score.project': 100}}
        setTo = {'$push': {'quiz': 20}}
        db['danupol'].update_one(where, setTo)


def airbnb_no_of_reviews():
    # เก็บลง List แล้ว sort
    with pymongo.MongoClient(connectMyMongoDB) as conn:
        db = conn.get_database('sample_airbnb')
        where = {}
        cursor = db['listingsAndReviews'].find(where)
        reviews = []
        for i in cursor:
            reviews.append({'name': i['name'], 'reviews_count': len(i['reviews'])})
        reviews = sorted(reviews, key=lambda k: k['reviews_count'], reverse=True)
        for i in reviews:
            print('Place = {}\nTotal Comment = {}'.format(i['name'], i['reviews_count']))
            print('-' * 50)
    # With aggregate sort
    # localhost เพราะ cloud ram ไม่พอใช้
    # with (pymongo.MongoClient('localhost', 27017)) as conn:
    #     # with pymongo.MongoClient(connectMyMongoDB) as conn:
    #     # db = conn.get_database('sample_airbnb')
    #     db = conn.get_database('Desktop')
    #     order_by = {'$sort': {'reviews_count': -1}}
    #     cursor = db['listingsAndReviews'].aggregate(
    #         [{'$project': {'name': 1, 'reviews': 1, 'reviews_count': {'$size': '$reviews'}}}, order_by])
    #     for i in cursor:
    #         print('Place = {}\nTotal Comment = {}'.format(i['name'], len(i['reviews'])))
    #         print('-' * 50)


def see_reviews(place):
    with pymongo.MongoClient(connectMyMongoDB) as conn:
        db = conn.get_database('sample_airbnb')
        where = {'name': place}
        name = db['listingsAndReviews'].find(where)
        for i in name:
            print('Place = {}'.format(i['name']))
        reviews = db['listingsAndReviews'].find(where)
        count = 1
        for i in reviews:
            for comment in i['reviews']:
                print('{}). {}'.format(count, comment['comments']))
                count += 1


def export_air_bnb_location():
    address = []
    with pymongo.MongoClient(connectMyMongoDB) as conn:
        db = conn.get_database('sample_airbnb')
        where = {'address.location.is_location_exact': True}
        cursor = db['listingsAndReviews'].find(where)
        for i in cursor:
            address.append([i['name'], i['address']['country'], i['address']['location']['coordinates'][1],
                            i['address']['location']['coordinates'][0]])
    with open('./MyTextFile/data_air_bnb.csv', mode='w', encoding='utf-8', newline='') as fn:
        fw = csv.writer(fn, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
        header = ['Place', 'Country', 'Latitude', 'Longitude']
        fw.writerow(header)
        fw.writerows(address)


def show_average_score():
    res_id = input('กรอก restaurant_id ที่ต้องการดูคะแนนเฉลี่ย : ')
    with pymongo.MongoClient(connectMyMongoDB) as conn:
        db = conn.get_database('sample_restaurants')
        where = {'restaurant_id': res_id}
        cursor = db['restaurants'].find(where)
        count = 1
        total = 0
        for i in cursor:
            print('{}\n'.format(i['name']))
            for value in i['grades']:
                print('Score {} = {}'.format(count, value['score']))
                count += 1
                total += value['score']
            print('\nAVERAGE = {:.2f}'.format(total / len(i['grades'])))


def comment_mflex():
    movie = input('หนังที่ต้องการ Comment : ')
    name = input('ชื่อ : ')
    lastname = input('นามสกุล : ')
    email = input('E-mail : ')
    comment = input('Comment ว่า : ')
    with pymongo.MongoClient(connectMyMongoDB) as conn:
        db = conn.get_database('sample_mflix')
        where = {'title': movie}
        found = db['movies'].count_documents(where)
        if found == 0:
            print('ไม่พบหนังที่เลือก')
            return
        db['comments'].insert_one(
            {'name': name + ' ' + lastname, 'email': email, 'mov"The Great Train Robbery"ie_id': 'xxxx',
             'date': datetime.now()})


if __name__ == '__main__':
    # export_student()
    # import_student()
    # testUpdateMany()
    # testRemove()
    # air_bnb()
    # cleaning_fee()
    # setNewDataToStudent()
    # airbnb_no_of_reviews()
    # see_reviews('Horto flat with small garden')
    # export_air_bnb_location()
    # show_average_score()
    comment_mflex()
