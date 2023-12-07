

def f(val):
  copy_val = val
  sum_dig = 0
  while copy_val > 0:
    sum_dig += copy_val % 2
    copy_val //= 2
  
  val = val*2 + sum_dig%2
  val *= 2
  return val

for x in range(100):
  t = f(x)
  if t > 43:
    print(t)
    break