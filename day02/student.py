# coding:utf-8

'''
    学生信息库
'''

stundets = {
    1:{
        'name':"whldk",'age':25, 'sex':'boy'
    },
    2:{
        'name':"whzs",'age':26, 'sex':'boy'
    },
    3:{
        'name':"whmw",'age':27, 'sex':'boy'
    }
}

#print(stundets)


def get_all_students():
    for id, value in stundets.items():
        print(
            '学号: {}, 姓名:{}, 年龄: {}, 性别: {}' . format(id, value['name'], value['age'], value['sex'])
        )
    return stundets

#res = get_all_students()

def add_student(**kwargs):
    if 'name' not in kwargs:
        print('缺少姓名')
        return
    if 'age' not  in kwargs:
        print('缺少年龄')
        return
    if 'sex' not  in kwargs:
        print('缺少性别')
        return
    id_ = max(stundets) + 1
    stundets[id_] = {
        'name' : kwargs['name'],
        'age' : kwargs['age'],
        'sex' : kwargs['sex']
    }


add_student(name='whzcl', age = 30, sex = 'girl')


def delete_student(id):
    if id not in stundets:
        print('id 不存在')
        return
    else:
        userinfo = stundets.pop(id)
        print(
            '删除--学号: {}, 姓名:{}'.format(id, userinfo['name'])
        )



def updated_student(id, **kwargs):
    if id not in stundets:
        print('不存在: {} 这个学号' . format(id))
        return
    if 'name' in kwargs:
        stundets[id]['name'] = kwargs['name']

    if 'age' in kwargs:
        stundets[id]['age'] = kwargs['age']

    if 'sex' in kwargs:
        stundets[id]['sex'] = kwargs['sex']

    print('更新同学信息成功')


# delete_student(1)

updated_student(1, age = 18, test =1)

#get_all_students()

def get_user_by_id(id):
    return stundets.get(id)

def get_user_by_where(**kwargs):
    values = list(stundets.values())
    key = None
    value = None
    result = []

    if 'name' in kwargs:
        key = 'name'
        value = kwargs['name']
    elif 'age' in kwargs:
        key = 'age'
        value = kwargs['age']
    elif 'sex' in kwargs:
        key = 'sex'
        value = kwargs['sex']
    else:
        print('没有发现搜索的关键字')

    for user in values:
        if user[key] == value:
            result.append(user)

    return result


a = get_user_by_where(sex='boy')
