from functools import lru_cache
def moves(x):
  return [x + 1, x + 4, x*5]

def go(x):
  return list(map(f, moves(x)))

@lru_cache(None)
def f(x):
  if x >= 68:
    return -0
  
  mas = go(x)

  if all(v > 0 for v in mas):
    return -max(mas) - 1
  else:
    return -max(v for v in mas if v <= 0) + 1

print("problem 19")
for s in range(1, 68):
  if +1 in go(s):
    print(s)
    break

print("problem 20")
for s in range(1, 68):
  if f(s) == +3:
    print(s)


print("problem 21")
for s in range(1, 68):
  if f(s) == -4:
    print(s)
    break

