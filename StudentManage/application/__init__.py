#项目初始化文件
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from redis import StrictRedis
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

from application.settings.dev import DevelopmentConfig
from application.settings.prop import ProductionConfig

config={
    'dev':DevelopmentConfig,
    'prop':ProductionConfig,

}

#增加日志模块
def setup_log(Config):
    #设置日志等级
    logging.basicConfig(level=Config.LOG_LEVEL)
    # 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
    file_log_handler=RotatingFileHandler('log/log',maxBytes=1024 * 1024 * 300, backupCount=10)
    # 创建日志记录的格式 日志等级 输入日志信息的文件名 行数 日志信息
    formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
    # 为刚创建的日志记录器设置日志记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象（flaskapp使用的）添加日志记录器
    logging.getLogger().addHandler(file_log_handler)

# 为了方便redis的连接对象在函数外部可以使用,预先设置一个全局变量,接下来在函数中用于保存redis的连接

redis_store=None

#创建数据库连接对象
db=SQLAlchemy()

def init_app(config_name):
    '项目初始化'
    #主应用的根目录
    app = Flask(__name__)

    #设置配置类
    Config=config[config_name]

    #加载配置
    app.config.from_object(Config)

    #redis的连接初始化
    global redis_store
    redis_store=StrictRedis(host=Config.REDIS_HOST,port=Config.REDIS_PORT,db=0)

    #开启CSRF防范
    CSRFProtect(app)

    #开启session
    Session(app)

    #增加数据库连接
    db.init_app(app)

    #启用日志
    setup_log(Config)

    #todo 注册蓝图
    from .apps.index import index_blu
    app.register_blueprint(index_blu,url_prefix='')


    return app


