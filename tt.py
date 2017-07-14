import sys
import time


with open('home-assistant.log') as f:
    f.seek(0,2)
    while True:
        line = f.readline()
        if line:
            print(line)
        time.sleep(1)


