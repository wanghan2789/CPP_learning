import threading
class Test(object):
    _lock = threading.Lock()
    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(Test, '_ourflag'):
            with Test._lock:
                if not hasattr(Test, '_ourflag'):
                    Test._ourflag = object.__new__(cls)
        return Test._ourflag


if __name__ == '__main__':
    a = Test()
    print(a)
    b = Test()
    print(b)