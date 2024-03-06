f = open("26_8663.txt")

n = int(f.readline())

mas = []
for line in f:
  a, b = map(int, line.split())

  mas += [(a, b)]

mas.sort()

row = 0
cnt = 0

for i in range(1, len(mas) - 1):
  if mas[i - 1][0] == mas[i][0] and mas[i][0] == mas[i + 1][0]:
    if mas[i][1] - mas[i - 1][1] == 6 and mas[i + 1][1] - mas[i][1] == 6:
      row = mas[i][0]
      cnt += 1

print(row, cnt)

