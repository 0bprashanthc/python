import threading
import time

class Sthread(threading.Thread):
    def run(self):
        print(threading.current_thread())
        time.sleep(3)
        print("3")

if __name__ == "__main__":
    for x in range(4):
        st = Sthread(name=str(x))
        st.start()
