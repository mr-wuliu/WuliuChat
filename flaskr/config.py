DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWORD = '123'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'webchat'

#mysql 不会认识utf-8,而需要直接写成utf8
SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT,DRIVER,USERNAME,PASSWORD,HOST,PORT,DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True

# 加密密钥
SECRET_KEY = 'DkCuMcr7qRsLJxKU'

# bootstrap使用本地资源
BOOTSTRAP_SERVE_LOCAL = True