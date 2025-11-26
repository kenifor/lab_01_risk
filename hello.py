import sys,base64 as b,os
p=lambda x:sys.stdout.write(x)
p(b.b64decode(b'SGVsbG8gYXBwc2Vjd29ybGQ=\n').decode())
