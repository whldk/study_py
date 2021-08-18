# coding:utf-8

import sys
import  os
# modules = sys.modules
# print(modules)
# path = sys.path
# print(path)
# print(sys.version)
# command = sys.argv[1]
# print(command)
#sys.exit(1)


def create_package(path):
    if os.path.exists(path):
        raise Exception('%s 已经存在不可创建' % path)
    os.makedirs(path)
    init_path = os.path.join(path, '__init__.py')
    f = open(init_path, 'w')
    f.write('# coding:utf-8\n')
    f.close()


class Open(object):
    def __init__(self, path, mode = 'w', is_return=True):
        self.path = path
        self.mode = mode
        self.is_return = is_return

    def write(self, message):
        f = open(self.path, mode=self.mode)
        if self.is_return:
            message = '%s\n'% message
        f.write(message)
        f.close()




if __name__ == '__main__':
    curr_path = os.getcwd()
    #增加目录
    #path = os.path.join(curr_path, 'test1')
    #create_package(path)
    open_path = os.path.join(curr_path, 'a.txt')
    o = Open(open_path)
    o.write('你好')


