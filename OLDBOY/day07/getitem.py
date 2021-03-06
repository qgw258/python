__author__ = 'qgw'

class Foo(object):
    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        print('__getitem__', key)
        return self.data.get[key]

    def __setitem__(self, key, value):
        print('__setitem__', key, value)
        self.data[key] = value

    def __delitem__(self, key):
        print('__delitem__', key)

obj = Foo()

# result = obj['k1']  # 自动触发执行 __getitem__
obj['name'] = 'alex'  # 自动触发执行 __setitem__
# print(obj['name'])
print(obj.data)
del obj['qwe']