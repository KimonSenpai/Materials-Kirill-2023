

def to_str(x: int, base: int)->str:
  ans = ''
  while x > 0:
    ans = str(x % base) + ans
    x //= base

  return ans


val = 36**7 + 6**19 - 18
s = to_str(val, 6)

print(s)

print(s.count("5"))