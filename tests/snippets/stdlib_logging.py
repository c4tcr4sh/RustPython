
import io
import sys

print("A")

f = io.StringIO()
sys.stderr = f
print("B")

import logging

print("C")
logging.error('WOOT')
print("CA")
logging.warning('WARN')
print("D")

res = f.getvalue()

assert  'WOOT' in res
assert  'WARN' in res
print(res)

