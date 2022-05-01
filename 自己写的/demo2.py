import time
import base64
time1 = str(int(time.time())/1000).encode("utf-8")
print(time1)
#转字节
print(base64.b64encode(bytes(time1)))

