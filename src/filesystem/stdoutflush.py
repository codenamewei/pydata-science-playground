import sys
import time

for i in range(1,10 ):
    sys.stdout.write(str(i))

time.sleep(10)
sys.stdout.flush()
print("\nEnd...")