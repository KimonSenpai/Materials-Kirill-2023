f = open("26_2362 (1).txt")

N, S = map(int, f.readline().split())

mas = {}
for i in range(N):
  a, b = map(int, f.readline().split())
  if a not in mas:
    mas[a] = []

  mas[a].append(b)

cnt = 0
min_cost = 0

for key in mas:
  #mas[key].sort()
  
  mass = mas[key]
  mass.sort()
  s = S
  i = 0
  while i < len(mass) and s >= mass[i]:
    s -= mass[i]
    min_cost += mass[i]
    cnt += 1
    i += 1
  
print(cnt, min_cost)