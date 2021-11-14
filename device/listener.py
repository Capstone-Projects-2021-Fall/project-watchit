import socket
import threading
import errno
import time

class Listener():

    def __init__(self, socket):
        self.socket = socket
        self.record = False

    def start(self):
        self.thread = threading.Thread(target=self.__listening).start()

    def __listening(self):
        while True:
            try:
                msg = self.socket.recv(1024).decode()
            except socket.error as e:
                err = e.args[0]
                if err == errno.EAGAIN or err == errno.EWOULDBLOCK:
                    continue
                else:
                    print(e)
                    exit(1)
            else:
                if msg == 'Record':
                    self.record = True
                elif msg == "Close":
                    self.stop()
            time.sleep(0.5)

    def stop(self):
        self.socket.close()
        self.thread.join()