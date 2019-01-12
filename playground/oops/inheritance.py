class parent:
    name = "parent"

    def __init__(self):
        pass
    
    def setname(self, name):
        self.name = name

    def run(self, speed):
        return self.name+" is running at a speed of "+str(speed)


class child(parent):
    def __init__(self, name):
        self.name = name

    def run(self):
        return self.name+" is running!"

class grandchild(child):
    def __init__(self):
        pass

class grandchild2(child):
    def __init__(self):
        pass

if __name__=="__main__":
    p = parent()
    print p.name
    p.setname("prashanth")
    print p.name
    print p.run(10)

    c = child("child")
    print c.name
    #c.setname("surabhi")
    print c.run()

    gc = grandchild()
    print gc.name

    gc2 = grandchild2()
    gc2.setname("grandchild2")
    print gc2.run()

    print "isinstance(p, parent) => ",isinstance(p, parent)
    print "isinstance(p, child) => ",isinstance(p, child)
    print "isinstance(c, parent) => ",isinstance(c, parent)
    print "isinstance(c, child) => ",isinstance(c, child)
    print "isinstance(gc, parent) => ",isinstance(gc, parent)
    print "isinstance(gc, child) => ",isinstance(gc, child)
    print "isinstance(gc, grandchild) => ",isinstance(gc, grandchild)
    print "isinstance(gc2, parent) => ",isinstance(gc2, parent)
    print "isinstance(gc2, child) => ",isinstance(gc2, child)
    print "isinstance(gc2, grandchild2) => ",isinstance(gc2, grandchild2)
    print "isinstance(gc2, grandchild) => ",isinstance(gc2, grandchild)
