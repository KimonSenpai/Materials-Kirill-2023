f = open("17_2024.txt")

mas = list(map(int, f))

mx = max(v for v in mas if (v % 100 == 21 and 10000 <= v < 100000))**2
cnt = 0
max_sum = 0

for i in range(1, len(mas)):
  x, y = mas[i-1], mas[i]

  if (x % 100 == 21 and 10000 <= x < 100000) + (y % 100 == 21 and 10000 <= y < 100000) == 1:
    if x*x + y*y >= mx:
      cnt += 1
      max_sum = max(max_sum, x + y)


print(cnt, max_sum)