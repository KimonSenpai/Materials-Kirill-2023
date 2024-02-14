from functools import lru_cache

def moves(x, y):
  return [(x + 1, y), (x, y + 1), (x*2, y), (x, y*2)]

def go(x, y):
  return list(map(f, moves(x, y)))

@lru_cache(None)
def f(xy):
  x, y = xy
  if x + y >= 77:
    return -0
  
  mas = go(x, y)

  if all(v > 0 for v in mas):
    return -max(mas) - 1
  else:
    return -max(v for v in mas if v <= 0) + 1
  
print("problem 19")
for s in range(1, 70):
  if +1 in go(7, s):
    print(s)
    break

print("problem 20")
for s in range(1, 70):
  if f((7, s)) == +3:
    print(s)
   

print("problem 21")
for s in range(1, 70):
  if f((7, s)) == -4:
    print(s)
    break
