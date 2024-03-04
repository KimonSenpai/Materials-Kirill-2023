# 123*567?

import regex as re

r = re.compile("123.*567.")

for val in range(10**3, 10**6):
  val = int("123" + str(val))
  if r.fullmatch(str(val)) and val % 169 == 0:
    print(val, val // 169)