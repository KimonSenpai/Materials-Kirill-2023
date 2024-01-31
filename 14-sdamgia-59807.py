
def f(x):
  return int("805678", base=25) + int("457069", base=25) + int("14501", base=25)\
  + x*25**4 + x*25**2 + x*25

for x in range(0, 17):
  val = f(x)
  if val % 23 == 0:
    print(val//23)