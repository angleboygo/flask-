from  redis import StrictRedis

#全局通用配置类
class Config(object):
    """项目配置核心类"""
    #调试模式
    DEBUG=True

    #todo 配置日志
    LOG_LEVEL = "DEBUG"

    #mysql数据库配置信息(指定字符集?charset=utf8)
    #数据库连接格式
    'SQLALCHEMY_DATABASE_URI ="数据库类型://用户名:密码@ip:port:库名?指定字符集编码"'
    SQLALCHEMY_DATABASE_URI = "mysql://root:123@127.0.0.1:3306/students?charset=utf8"
    # 动态追踪修改设置，如未设置只会提示警告
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 查询时会显示原始SQL语句
    SQLALCHEMY_ECHO = False

    # 配置redis
    # 项目上线以后，这个地址就会被替换成真实IP地址，mysql也是
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379

    #设置session 秘钥
    #可以通过 base64.b64encode(os.urandom(48)) 来生成一个指定长度的随机字符串
    SECRET_KEY = "CF3tEA1J3hRyIOw3PWE3ZE9+hLOcUDq6acX/mABsEMTXNjRDm5YldRLIXazQviwP"

    #flask_session的配置信息
    SESSION_TYPE='redis' #指定session保存到redis中
    SESSION_USE_SIGNER=True # 让 cookie 中的 session_id 被加密签名处理
    SESSION_REDIS=StrictRedis(host=REDIS_HOST,port=REDIS_PORT) # 使用 redis 的实例
    PERMANENT_SESSION_LIFETIME = 24 * 60 * 60  # session 的有效期，单位是秒
