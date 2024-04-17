f = open("26_9847.txt")


N = int(f.readline())

events = []

for line in f:
  fr, to = map(int, line.split())
  events += [(fr, 1), (to, -1)]

events.sort()

max_count = 0
peaks = 0
cnt = 0

for t, type in events:
  if type == 1:
    cnt += 1
    if max_count < cnt:
      max_count = cnt
      peaks = 0
    elif max_count == cnt:
      peaks += 1

  else:
    cnt -= 1

print(max_count, peaks)


1 100
100 200
99 101
