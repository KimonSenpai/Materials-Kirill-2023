f = open("1_27_A.txt")


min_cost = 10**20

n = int(f.readline())
mas = [int(line) for line in f]

for i in range(n):
  cost = 0
  for j in range(n):
    cost += mas[j] * min((i - j) % n, (j - i) % n)

  min_cost = min(min_cost, cost)

print(min_cost)