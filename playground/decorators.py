def is_decorator(func):
    def _func():
        print "inside decorator"
        func()
    return _func

@is_decorator
def a():
    print "inside a()"

a()
