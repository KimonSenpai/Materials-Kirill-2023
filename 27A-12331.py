f = open("27A_12331.txt")

n = int(f.readline())
T = int(f.readline())
mas = [int(line) for line in f]

sum_cost = 0
for i in range(n):
  cost = 0
  for j in range(max(0, i - T), min(n, i + T + 1)):
    cost = max(cost, mas[j]*abs(i - j))

  sum_cost += cost

print(sum_cost)