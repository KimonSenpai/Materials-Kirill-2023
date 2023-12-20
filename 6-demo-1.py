from math import tan, pi

k = tan(pi/6)

def y1(x):
  return k*x

def y2(x):
  return -k*x + 10
cnt = 0
for y in range (1, 11):
  for x in range(1, 11):
    if y > y1(x) and y < y2(x):
      cnt += 1

print(cnt)

