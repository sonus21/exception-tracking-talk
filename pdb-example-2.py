import pdb
import random
import sys


class Foo(object):
    def go(self, name):
        if random.randint(1, 10) == 1:
            raise ValueError("I'm evil")
        print("Hi {name}".format(name=name))


class Demo(object):
    def hi(self, name):
        Foo().go(name)


d = Demo()
try:
    for i in range(100):
        d.hi(str(i))
except Exception as e:
    ex, value, tb = sys.exc_info()
    pdb.post_mortem(tb)
