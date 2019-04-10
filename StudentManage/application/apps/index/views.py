#index蓝图的视图
from application import db
from application.apps.index.models import Student
from .  import index_blu
from flask import render_template, request, flash


@index_blu.route('/')
def index():
    return render_template('index.html')

@index_blu.route('/test')
def test():
    '测试静态文件'
    return render_template('test.html')


#显示学生信息
@index_blu.route('/students')
def students():
    """學生列表"""
    student_list = Student.query.all()
    data = []
    for student in student_list:
        print(student.sex)
        data.append({
            "id": student.id,
            "name": student.name,
            "age": student.age,
            "sex": "男" if student.sex else "女",
            "description": student.description,
            "class_number": student.class_number,
        })

    return render_template("students.html", students=data)


@index_blu.route("/add",methods=["POST","GET"])
def add_student():
    if request.method == "POST":
        # 接受數據
        name = request.form.get("username")
        age = int( request.form.get("age") )if request.form.get("age") else 0
        sex = True if request.form.get("sex") == '1' else False
        class_number = request.form.get("class_number")
        description = request.form.get("description")
        # 驗證數據
        if age < 0 or age > 120:
            # 閃現信息[用於返回錯誤信息給客戶端,只顯示一次]
            flash("非法的年齡數值")

        # 保存入庫
        student = Student(name=name,age=age,sex=sex,class_number=class_number,description=description)
        try:
            db.session.add(student)
            db.session.commit()
        except:
            # 事務回滾
            db.session.rollback()

    return render_template("add_students.html")
