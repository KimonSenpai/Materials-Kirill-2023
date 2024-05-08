f = open("27-B_3231.txt")

N = int(f.readline())

c = [int(f.readline()) for _ in range(N)]

cost = 0
left = 0
right = 0

for i in range(1, N//2 + 1):
  cost += c[i]*i
  right += c[i]

for i in range(0, N//2):
  cost += c[-i]*i
  left += c[-i]

min_cost = cost
point = 0

for i in range(1, N):
  cost += -right + left

  if cost < min_cost:
    min_cost = cost
    point = i
  
  opos = (i + N//2) % N
  left += c[i] - c[opos]
  right += -c[i] + c[opos]

print(point + 1)