import sys
import time

for i in range(1,10 ):
    print(str(i), end = "")

time.sleep(10)
sys.stdout.flush()
print("End...")