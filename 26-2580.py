f = open('26_2580.txt')

n, k = map(int, f.readline().split())

END = 10**20

L, K,  R = 1, 0, -1

events = [(k, K)]

for line in f:
  tin, tout = map(int, line.split())
  if tout == 0:
    tout = END
  
  events += [(tin, L)] + [(tout, R)]

events.sort()


is_k = False
t_last = 0
count = 0
max_count = 0
max_dur = 0

for t, type in events:
  if type == L:
    count += 1
    t_last = t
  elif type == K:
    is_k = True
    t_last = t
  else:
    if is_k:
      if count > max_count:
        max_count = count
        max_dur = t - t_last
      elif count == max_count:
        max_dur = max(max_dur, t - t_last)

    count -= 1

print(max_count, max_dur)

