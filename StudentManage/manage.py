from application import init_app,db
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand


app=init_app('dev')

#使用终端管理工具
manager=Manager(app)

#使用数据迁移工具
Migrate(app,db)

#添加数据库迁移命令到终端脚本工具中
manager.add_command('db',MigrateCommand)

# 导入模型[为了进行数据迁移]
from application.apps.index.models import Student

@app.route('/')
def index():
    return 'index'

if __name__ == '__main__':
    manager.run()