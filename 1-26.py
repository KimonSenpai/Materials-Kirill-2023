f = open("1_26.txt")

n = int(f.readline())

mas = [int(line) for line in f]

mas.sort(reverse=True)

last = 10**5
cnt = 0

for size in mas:
  if last - size >= 4:
    cnt += 1
    last = size

print(cnt, last)