
"""
放入資料庫密碼
"""


class MongoBase:
    username = "root"
    password = "showmethemoney"
    authSource = "res"
    authMechanism = 'SCRAM-SHA-256'


class MyAccount:
    account = "Guestiii"
    passwd = "iiiedu"
    host = "test.csk2mdrch6yp.ap-northeast-1.rds.amazonaws.com"