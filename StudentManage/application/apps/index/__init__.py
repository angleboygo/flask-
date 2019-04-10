from flask import Blueprint

#声明蓝图
'''
template_folder:指定模板文件路径,查找顺序,先全局templates里面找,没找到,再往子蓝图里面找.

'''
#给app取别名为 'index'
index_blu=Blueprint('index',__name__,template_folder='templates',static_folder='static')

from .views import *

