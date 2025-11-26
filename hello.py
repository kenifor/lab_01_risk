import sys,base64 as b
p=lambda x:sys.stdout.write(x)
p(b.b64decode(b'SGVsbG8gYXBwc2Vjd29ybGQ=').decode()+f' from {sys.stdin.readline().strip()}\n')
