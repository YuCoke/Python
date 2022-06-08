import datetime

import requests
import json
import sql_connect
from datetime import timedelta

'''
获取阅读数
'''


def getUserRead(token, beginDate, endDate):
    url = 'https://api.weixin.qq.com/datacube/getuserread?access_token=' + token
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

    def save(self, read):
        data = (read['user_source'], read['ref_date'], read['int_page_read_user'],
                read['int_page_read_count'], read['ori_page_read_user'], read['ori_page_read_count'],
                read['share_user'], read['share_count'], read['add_to_fav_user'], read['add_to_fav_count'], gh_id)
        sql = "insert into `read`(user_source,date, read_user,read_count,ori_page_read_user,ori_page_read_count, " \
              "share_user, share_count, add_to_fav_user, add_to_fav_count, gh_id) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        print(sql, data)
        self.connect.run(sql, data)

    def run(self):
        start_date = datetime.date.today()
        start_date = start_date + timedelta(-1)
        date = start_date.strftime('%Y-%m-%d')
        reads = getUserRead(self.access_token, date, date)
        for a in reads:
            self.save(a)

        self.connect.close()


if __name__ == '__main__':
    gh_id = 'gh_f176fe49e5c4'
    app_id = 'wx8ae21ace9c0c7b5d'
    secret = '479ce3b4621a9dd320d87c58304a7faf'
    sub = getSubscription()
    sub.run()
