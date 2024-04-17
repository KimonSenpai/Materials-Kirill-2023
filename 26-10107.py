f = open("26_10107.txt")


N = int(f.readline())

events = []

for line in f:
  fr, to = map(int, line.split())
  events += [(fr, to)]


events.sort(key=lambda x: tuple(reversed(x)))

last = 0
lastlast = 0
cnt = 0

for fr, to in events:
  if fr >= last:
    cnt += 1
    lastlast = last
    last = to

mx = max(fr for fr, to in events)

print(cnt, mx - lastlast)
