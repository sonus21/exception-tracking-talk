import random
from error_tracker import print_exception


class Foo(object):
    def go(self, name):
        if random.randint(1, 10) == 1:
            raise ValueError("I'm evil")
        print("Hi {name}".format(name=name))


class Demo(object):
    def hi(self, name):
        Foo().go(name)


d = Demo()
for i in range(100):
    try:
        d.hi(str(i))
    except Exception as e:
        print_exception()
        break
