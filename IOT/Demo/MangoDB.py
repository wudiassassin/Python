import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)
db = client["test"]
collection = db["students"]
student = {
    'id': '20170102',
    'name': 'Mike',
    'age': 21,
    'gender': 'male'
}

# insert = collection.insert_one(student)   # 插入数据
# print(insert.inserted_id)

results = collection.find({'name': 'Mike'})    # 查询
for result in results:
    print(result)

count = collection.estimated_document_count()   # 计数
# count = collection.count_documents({'name': 'Mike'})
print(count)

sorts = collection.find().sort('name', pymongo.ASCENDING).skip(1).limit(2)   # 排序+偏移
print([sort['name'] for sort in sorts])

condition = {'age': {'$gt': 20}}    # 更新
update = collection.update_many(condition, {'$inc': {'age': 1}})
print(update.matched_count, update.modified_count)

delete = collection.delete_one({'name': 'Mike'})    # 删除

