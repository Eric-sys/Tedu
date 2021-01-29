"""
第一种方案
"""


f = open('file','wb')

f.write(b'a')
f.seek(1024)
f.write(b'b')

f.close()