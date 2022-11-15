from urllib.parse import urlencode
import requests
from pyquery import PyQuery as pq
from pymongo import MongoClient

base_url = 'https://m.weibo.cn/api/container/getIndex?'
headers = {
    'Host': 'm.weibo.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52',
    'X-Requested-With': 'XMLHttpRequest',
}
max_page = 10
client = MongoClient()
db = client['test']
collection = db['weibo']


def get_page(page):
    params = {
        'type': 'uid',
        'value': '2830678474',
        'containerid': '1076032830678474',
        'page': page
    }
    url = base_url + urlencode(params)
    try:
        re = requests.get(url,headers=headers)
        if re.status_code == 200:
            return re.json()
    except requests.ConnectionError as e:
        print('Error', e.args)


def parse_page(json):
    if json:
        items = json.get('data').get('cards')
        for item in items:
            item = item.get('mblog')
            weibo = {}
            weibo['id'] = item.get('id')
            weibo['text'] = pq(item.get('text')).text()
            weibo['attitudes'] = item.get('attitudes_count')
            weibo['comment'] = item.get('comment_count')
            weibo['reports'] = item.get('reports_count')
            yield weibo


def save_to_mongo(result):
    if collection.insert_one(result):
        print('Save to Mongo')


if __name__ == '__main__':
    for page in range(1, max_page+1):
        json = get_page(page)
        results = parse_page(json)
        for result in results:
            print(result)
            save_to_mongo(result)

