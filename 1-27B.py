f = open("1_27_B.txt")


min_cost = 10**20

n = int(f.readline())
mas = [int(line) for line in f]

l_sum = 0
r_sum = 0
cost = 0

for i in range(1, n//2 + 1):
  cost += i*mas[i]
  r_sum += mas[i]

for i in range(0, n//2):
  cost += i*mas[-i]
  l_sum += mas[-i]

min_cost = cost

for i in range(1, n):
  cost += l_sum - r_sum

  min_cost = min(min_cost, cost)

  opos = (i + n//2) % n

  l_sum += mas[i] - mas[opos]
  r_sum += -mas[i] + mas[opos]

print(min_cost)