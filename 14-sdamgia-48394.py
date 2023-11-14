

def f(x):
  return 4*15**0 + x*15**1 + 12*15**2 + 4*15**3 + 10 + 2*13 + 6*13**2 + x*13**3


for x in range(12):
  if f(x) % 121 == 0:
    print(f(x) // 121)
    break