f = open("27B_12331.txt")

n = int(f.readline())
T = int(f.readline())
mas = [int(line) for line in f]

ind = [[] for i in range(10)]

for i in range(n):
  ind[mas[i]] += [i]

l = [0]*10
r = [-1]*10

sum_cost = 0

for i in range(n):
  cost = 0
  for d in range(1, 10):
    if len(ind[d]) == 0: continue
    if ind[d][l[d]] - i > T: continue

    while l[d] + 1 < len(ind[d]) and ind[d][l[d] + 1] < i and i - ind[d][l[d]] > T:
      l[d] += 1
    while r[d] + 1 < len(ind[d]) and ind[d][r[d] + 1] - i <= T:
      r[d] += 1
    if abs(i - ind[d][l[d]]) <= T:
      cost = max(cost, d*abs(i - ind[d][l[d]]))
    if abs(ind[d][r[d]] - i) <= T:
      cost = max(cost, d*abs(ind[d][r[d]] - i))
    

  sum_cost += cost

print(sum_cost)