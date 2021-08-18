# coding:utf-8
"""
    学生信息库类
"""
class StudentInfo(object):

    def __init__(self, students):
        self.students = students

    def __setattr__(self, key, value):
        self.__dict__[key] = value


    def search(self, **student):
        values = list(self.students.values())
        key = None
        value = None
        result = []
        if 'name' in student:
            key = 'name'
            value = student['name']
        elif 'age' in student:
            key = 'age'
            value = student['age']
        elif 'sex' in student:
            key = 'sex'
            value = student['sex']
        elif 'classinfo' in student:
            key = 'classinfo'
            value = student['classinfo']
        else:
            print('没有发现搜索的关键字')

        for user in values:
            if user[key] == value:
                result.append(user)
                print(
                    '姓名:{}, 年龄: {}, 性别: {}, 班级: {}'.format(user['name'], user['age'], user['sex'],user['classinfo'])
                )


    def list(self):
        for id, value in self.students.items():
            print(
                '学号: {}, 姓名:{}, 年龄: {}, 性别: {}, 班级: {}'.format(id, value['name'], value['age'], value['sex'], value['classinfo'])
            )

    def create(self, **student):
        check = self.check_user_info(**student)
        if check != True:
            print(check)
            return
        id_ = max(self.students) + 1
        self.students[id_] = {
            'name': student['name'],
            'age': student['age'],
            'sex': student['sex'],
            'classinfo': student['classinfo']
        }
        return id_

    def more_create(self, more_studens):
        for student in more_studens:
            check = self.check_user_info(**student)
            if check != True:
                print(check, student.get('name'))
                continue
            self.create(**student)

    def delete(self, id):
        if id not in self.students:
            print('id 不存在')
            return
        else:
            userinfo = self.students.pop(id)
            print(
                '删除学生信息-学号: {}, 姓名:{}, 班级: {}'.format(id, userinfo['name'], userinfo['classinfo'])
            )

    def upadate(self, **student):
        if id not in self.students:
            print('请输入正确的: {} 学号ID'.format(id))
            return
        check = self.check_user_info(**student)
        if check != True:
            print(check)
            return
        self.students[id] = student
        return id

    def view(self, id):
        return self.students.get(id)

    def check_user_info(self, **student):
        if 'name' not in student:
            print('缺少姓名')
            return
        if 'age' not in student:
            print('缺少年龄')
            return
        if 'sex' not in student:
            print('缺少性别')
            return
        if 'classinfo' not in student:
            print('缺少班级')
            return
        return True


# 设置学生列表信息
students = {
    1:{'name': "whldk", 'age': 18, 'sex': 'boy', 'classinfo':'测试1班'},
    2:{'name': "whzs", 'age': 19, 'sex': 'boy', 'classinfo':'测试2班'},
    3:{'name': "whmw", 'age': 20, 'sex': 'boy', 'classinfo':'测试3班'}
}

#初始化运行
if __name__ == '__main__':
    student = StudentInfo(students)

    #添加学生
    id = student.create(name='韩棒',age=18,sex='boy', classinfo='测试三班')
    #print(id)  # id = 4
    #查看学生 4
    #user = student.view(4)
    #print(user)    #{'name': '韩棒', 'age': 18, 'sex': 'boy', 'classinfo': '测试三班'}

    #批量添加
    users = [{'name': "whldk1", 'age': 18, 'sex': 'boy', 'classinfo':'测试1班'},{'name': "whldk2", 'age': 18, 'sex': 'boy', 'classinfo':'测试1班'}]
    student.more_create(users)

    #搜索学生条件信息
    student.search(classinfo='测试1班')