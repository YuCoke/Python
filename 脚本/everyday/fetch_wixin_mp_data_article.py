import datetime

import requests
import json
import sql_connect
from datetime import timedelta
'''
获取文章
'''


def getArticleTotal(token, beginDate, endDate):
    url = 'https://api.weixin.qq.com/datacube/getarticletotal?access_token=' + token
    payload = {'begin_date': beginDate, 'end_date': endDate}
    r = requests.post(url, json=payload)
    data = json.loads(r.content)
    return data['list']


def getAccessToken(appid, secret):

    url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential'
    payload = {'appid': appid, 'secret': secret}
    r = requests.get(url, params=payload)
    data = json.loads(r.content)
    return data['access_token']


class getSubscription:

    def __init__(self):
        self.connect = sql_connect.Connect()
        self.access_token = getAccessToken(app_id, secret)

    def save(self, article):
        data = (article['title'], article['ref_date'], article['msgid'], article['user_source'], article['url'], gh_id)
        sql = "insert into article(title,date, msgid,user_source,url, gh_id) values (%s,%s,%s,%s,%s,%s)"
        print(sql, data)
        # self.connect.run(sql, data)

    def run(self):
        start_date = datetime.date.today()
        start_date = start_date + timedelta(-1)
        date = start_date.strftime('%Y-%m-%d')
        articles = getArticleTotal(self.access_token, date, date)
        # print(len(articles))
        if len(articles) > 0:
            for a in articles:
                self.save(a)
        self.connect.close()


if __name__ == '__main__':
    gh_id = 'gh_f176fe49e5c4'
    app_id = 'wx8ae21ace9c0c7b5d'
    secret = '479ce3b4621a9dd320d87c58304a7faf'
    sub = getSubscription()
    sub.run()
