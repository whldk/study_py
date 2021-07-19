class Node():
    def __init__(self, value):
        self.data = value
        self.next = None


class Stack():
    def __init__(self):
        self.top = None

    def push(self, element):
        n = Node(element)
        n.next = self.top
        self.top = n

    def pop(self):
        if self.empty():
            print('栈空')
            return
        n = self.top
        self.top = self.top.next
        del n

    def getTop(self):
        if self.empty():
            print('栈是空的')
            return
        return self.top.data

    def empty(self):
        return self.top == None

    def clear(self):
        while self.top != None:
            temp = self.top
            self.top = self.top.next
            del temp

    def length(self):
        temp = self.top
        count = 0
        while temp != None:
            count += 1
            temp = temp.next
        return count

    def list(self):
        temp = self.top
        while temp != None:
            print(temp.data)
            temp = temp.next

    def find(self):


if __name__ == '__main__':
    stack = Stack()

    #添加
    stack.push("韩棒1")
    stack.push("韩棒2")
    stack.push("韩3")

    #查看个数 、获取最后一个插入的元素
    n = stack.length()
    #print(n)
    pop = stack.getTop()
    #print(pop)

    #移除
    pop = stack.pop()
    n = stack.length()
    #print(n)

    #列表
    stack.list()