# -*- coding: utf-8 -*-
# @Author  : ydf
# @Time    : 2019/10/8 0008 13:55
"""
单例模式
适用范围三颗星，这不是最常用的设计模式。往往只能脱出而出仅仅能说出这一种设计模式，但oop根本目的是要多例，
使用oop来实现单例模式，好处包括
1 延迟初始化（只有在生成对象时候调用__init__里面时候才进行初始化）
2 动态传参初始化
否则，一般情况下，不需要来使用类来搞单例模式，文件级模块全局变量的写法搞定即可，python模块天然单例，不信的话可以测试一下，c导入a，b也导入a，c导入b，在a里面直接print hello，
运行c.py,只会看到一次print hello。

"""


from monkey_print2 import print


class A:
    """
    # &&&&&这种方式重写new实现的单例模式要注意，虽然生成的对象都是同一个，但init会每次都被自动调用。py2这种写法实现的单例模式，init不会自动被调用，py3会被自动调用。
    要是init里面成本很大，不希望被自动调用，可以改成另外的方式，参考其他方式的单例模式。&&&&&
    修改上面这个缺点的重写new方式
    """
    _inst = None
    def __new__(cls, *args,**kwargs):
        if not cls._inst:
            cls._inst = object.__new__(cls)
            cls._inst.__custom_init__(*args,**kwargs)  # 重点在这里。
        return cls._inst

    def __custom_init__(self, identity):  # 这行也是是重点。去掉了__init__方法，init会被自动调用，改成在new里面主动调用。
        print('执行init')
        self.identity = identity

    def eat(self):
        print(f'{self.identity} 吃饭')


if __name__ == '__main__':
    a1 = A('001')
    a2 = A('001')
    print(a1 == a2)
    a1.eat()
    a2.eat()
    a3 = A('003')
    print(a1 == a3)
    a3.eat()

    """
    init只会执行一次。
"D:/coding2/python36patterns/创建型模式-单例模式-重写new但不每次执行init方式.py:33"  16:20:19  执行init
"D:/coding2/python36patterns/创建型模式-单例模式-重写new但不每次执行init方式.py:43"  16:20:19  True
"D:/coding2/python36patterns/创建型模式-单例模式-重写new但不每次执行init方式.py:37"  16:20:19  001 吃饭
"D:/coding2/python36patterns/创建型模式-单例模式-重写new但不每次执行init方式.py:37"  16:20:19  001 吃饭
"D:/coding2/python36patterns/创建型模式-单例模式-重写new但不每次执行init方式.py:47"  16:20:19  True
"D:/coding2/python36patterns/创建型模式-单例模式-重写new但不每次执行init方式.py:37"  16:20:19  001 吃饭


    """
