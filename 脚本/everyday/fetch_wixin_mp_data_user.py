import requests
import json
import sql_connect
from datetime import timedelta, datetime
'''
获取订阅人数
'''


def getUserSummary(token, beginDate, endDate):
    url = 'https://api.weixin.qq.com/datacube/getusersummary?access_token=' + token
    payload = {'begin_date': beginDate, 'end_date': endDate}
    r = requests.post(url, json=payload)
    data = json.loads(r.content)
    return data['list'][0]


def getUserCumulates(token, beginDate, endDate):
    url = 'https://api.weixin.qq.com/datacube/getusercumulate?access_token=' + token
    payload = {'begin_date': beginDate, 'end_date': endDate}
    r = requests.post(url, json=payload)
    data = json.loads(r.content)
    return data['list'][0]


def getAccessToken(appid, secret):
    url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential'
    payload = {'appid': appid, 'secret': secret}
    r = requests.get(url, params=payload)
    data = json.loads(r.content)
    return data['access_token']


def appendGhIdForList(list, gh_id):
    for item in list:
        item['gh_id'] = gh_id
    return list


class getSubscription:

    def __init__(self):
        self.connect = sql_connect.Connect()
        self.access_token = getAccessToken(app_id, secret)

    def save(self, summary, cumulates):
        data = (cumulates['cumulate_user'], cumulates['ref_date'], summary['new_user'], summary['cancel_user'], summary['user_source'], gh_id)
        sql = "insert into subscription_user(cumulate_user,date, new_user,cancel_user,user_source,gh_id) values (%s,%s,%s,%s,%s,%s,%s)"
        print(sql, data)
        self.connect.run(sql, data)

    def run(self):
        today = datetime.today()
        yesterday = today + timedelta(-1)
        date = yesterday.strftime('%Y-%m-%d')
        summary = getUserSummary(self.access_token, date, date)
        cumulates = getUserCumulates(self.access_token, date, date)
        self.save(summary, cumulates)
        self.connect.close()


if __name__ == '__main__':
    gh_id = 'gh_f176fe49e5c4'
    app_id = 'wx8ae21ace9c0c7b5d'
    secret = '479ce3b4621a9dd320d87c58304a7faf'
    sub = getSubscription()
    sub.run()

