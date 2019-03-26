class Service:
    name = None
    def __init__(self, name):
        self.name = name

    def run(self, speed):
        return self.name+" is running at a speed of "+str(speed)

    def cm(self):
        return self

    @staticmethod
    def static_foo(self):
        print "executing static_foo(%s)"%self

if __name__ == "__main__":
    service = Service("prashanth")
    print Service.static_foo(service)
