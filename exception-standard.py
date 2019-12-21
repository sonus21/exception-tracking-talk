import random
import sys
import traceback


class Demo(object):
    def hi(self, name):
        if random.randint(1, 10) == 1:
            raise ValueError("I'm evil")
        print("Hi {name}".format(name=name))


d = Demo()
for i in range(100):
    try:
        d.hi(str(i))
    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        traceback.print_tb(exc_traceback)
        break
