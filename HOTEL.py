import time
import numpy as np
import pandas as pd

import socket

class prog:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(("142.93.73.149",11159))
    def toStr(self, b):
        return bytes(b).decode()
    def send(self, str_data):
        str_data = str(str_data)
        self.s.send(str(str_data).encode())
    def getValu(self,a,b,n):
        x = np.arange(int(a), int(b)+1)
        return pd.Series(x).to_json(orient="records").count(str(n))
        #r = "".join([str(x) for x in range(int(a), int(b) + 1)])
        #t = 0
        #for x in r:
        #    if (int(n) == int(x)):
        #        t += 1
        #return t
    def run(self):
        print(self.toStr(self.s.recv(4096)))
        self.send("start")
        print(self.toStr(self.s.recv(4096)))
        r = True
        while r:
            print("Current date & time " + time.strftime("%c"))
            ar = str(self.toStr(self.s.recv(4096))).split("\n")
            a, b = str(ar[2]).replace("     Quartos: ", "").replace("[", "").replace("]", "").replace(" ", "").split(
                ",")
            n = str(ar[3]).split(" ")[-1]

            str_data = self.getValu(a, b, n)
            print(str("\n".join(ar)) + str(str_data))
            self.send(str_data)
            res = self.toStr(self.s.recv(4096))
            print(res)
            if "Acert" in res:
                continue
            else:
                r = False
            print("Current date & time " + time.strftime("%c"))
    def close(self):
        self.s.close()



if __name__ == '__main__':
    p = prog()
    p.run()
