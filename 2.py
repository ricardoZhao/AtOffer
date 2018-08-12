#!/usr/bin/env python3
# coding:utf-8

"""
实现singleton
"""
import threading


# 基于类实现
class Singleton(object):
    instance = None
    lock = threading.Lock()
    
    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            with cls.lock:
                if not cls.instance:
                    cls.instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls.instance


# 基于装饰器实现
def singleton(cls):
    instance = {}
    lock = threading.Lock()

    def _singleton(*args, **kwargs):
        if cls not in instance:
            with lock:
                if cls not in instance:
                    instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return _singleton


@singleton
class Test(object):
    
    def __init__(self, *args, **kwargs):
        pass


if __name__ == '__main__':
    a = Singleton()
    b = Singleton()
    print(a is b)

    a = Test()
    b = Test()
    print(a is b)
