#!/usr/bin/env python3
# coding:utf-8

"""
用两个栈实现一个队列，请实现append_tail和delete_head,
分别完成在队列尾部插入节点和队列头部删除节点的功能。
"""


class Stack(object):
    # 初始化栈为空列表
    def __init__(self):
        self.items = []

    # 判断栈是否为空，返回布尔值
    def is_empty(self):
        return self.items == []

    # 返回栈顶元素
    def peek(self):
        return self.items[len(self.items) - 1]

    # 返回栈的大小
    def size(self):
        return len(self.items)

    # 把新的元素堆进栈里面（程序员喜欢把这个过程叫做压栈，入栈，进栈……）
    def push(self, item):
        self.items.append(item)

    # 把栈顶元素丢出去（程序员喜欢把这个过程叫做出栈……）
    def pop(self):
        return self.items.pop()


class MyQueue(object):

    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def append_tail(self, val):
        self.stack1.push(val)

    def delete_head(self):
        if self.stack2.size():
            return self.stack2.pop()
        else:
            if not self.stack1:
                return
            while self.stack1.size():
                self.stack2.push(self.stack1.pop())
            return self.stack2.pop()


if __name__ == '__main__':
    q = MyQueue()
    for i in range(10):
        q.append_tail(i)

    for i in range(10):
        print(q.delete_head())
