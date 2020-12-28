show dbs;

use tni_new;
show collections;
db.createCollection('students');
db.createCollection('products');
db.dropDatabase();

db.students.insert({'id':'60121053-7','name':'Danupol'});
db.students.insert([{'id':'60121053-7','name':'Danupol1'},{'id':'60121053-7','name':'Danupol2'}]);
db.students.insert({'id':'60121054-1','name':'Malee','weight':87,'height':190});
db.students.insert({'id':'60121054-1','name':'Malee','WEIGHT':87,'height':190});
db.students.insert({'id':'60121054-1','name':'Malee','physical_data':{'WEIGHT':87,'height':190}});

db.students.find();
db.products.find();