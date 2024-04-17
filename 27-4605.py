f = open('27B_4605.txt')

n = int(f.readline())

mas = []
for line in f:
  a, b = map(int, line.split())
  b = b // 36 + (b % 36 != 0)
  mas += [(a, b)]

cur = 0
sum_left = 0
sum_right = 0

for i in range(0, n):
  sum_right += mas[i][1]
  cur += mas[i][1]*(mas[i][0] - mas[0][0])

ans = cur

for i in range(1, n):
  sum_left += mas[i - 1][1]
  sum_right -= mas[i - 1][1]
  delta = mas[i][0] - mas[i - 1][0]

  cur += sum_left*delta - sum_right*delta
  ans = min(ans, cur)

print(ans)