import re

r = re.compile("3.12.14.*5")


for val in range(1917, 10**10, 1917):
  if r.fullmatch(str(val)):
    print(val, val // 1917)