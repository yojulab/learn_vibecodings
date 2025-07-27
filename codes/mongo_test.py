import pymongo
from pymongo import MongoClient

# MongoDB 연결 정보
def get_mongo_client():
    return MongoClient('mongodb://db_mongodb:27017/')

def test_connection():
    try:
        client = get_mongo_client()
        db = client['test_db']
        col = db['test_collection']
        # 테스트용 데이터 삽입
        result = col.insert_one({'msg': 'MongoDB 연결 성공!'})
        # 데이터 조회
        doc = col.find_one({'_id': result.inserted_id})
        print('DB 연결 및 데이터 삽입/조회 성공:', doc)
    except Exception as e:
        print('MongoDB 연결 실패:', e)

if __name__ == '__main__':
    test_connection()
