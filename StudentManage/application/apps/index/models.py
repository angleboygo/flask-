# coding=utf-8

from application import db


# 创建关系表,不再创建模型,一般用于表与表之间的多对多场景(3)
"""
表关系变量 = db.Table(
    "关系表表名",
    db.Column('字段名', 字段类型, 字段选项),  # 普通字段
    db.Column("字段名", 字段类型, db.ForeignKey("表名.id")),
    db.Column("字段名", 字段类型, db.ForeignKey("表名.id")),
)
"""
achievement = db.Table(
    "achievement", #表名
    db.Column('score', db.Numeric, comment="分数"), #新增字段
    db.Column('student_id', db.Integer, db.ForeignKey('student.id')),
    db.Column('course_id', db.Integer, db.ForeignKey('course.id'))
)

class Student(db.Model):
    """学生信息(1)"""
    __tablename__ = "student" #设置表名
    id = db.Column(db.Integer, primary_key=True, comment="主键ID")
    name = db.Column(db.String(64), index=True, comment="姓名" )
    sex = db.Column(db.Boolean, default=True, comment="性别")
    class_number = db.Column(db.String(32), nullable=True, index=True, comment="班级")
    age = db.Column(db.SmallInteger, comment="年龄")
    description = db.Column(db.Text, comment="个性签名")
    #创建完多对多关系表后,再创建表之间的访问关系(4)
    courses = db.relationship(
        'Course', # 模型名称
        secondary=achievement, # 表关系变量
        backref='students', # 当外键反过来获取主键信息时,使用的字段名称,可以自定义,接下来的使用例如: course.students 获取某个课程下所有的学生
        lazy='dynamic'
    )

class Course(db.Model):
    """课程信息(2)"""
    __tablename__ = "course"
    id = db.Column(db.Integer, primary_key=True,comment="主键ID")
    name = db.Column(db.String(64), unique=True,comment="课程名称")