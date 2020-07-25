import threading

class SThread(threading.Thread):
    def run(self):
        print(self.name)
        a = 10
        print(threading.current_thread())

if __name__ == "__main__":
    t = SThread(name="bla")
    t.start()
    print(threading.local().a)
