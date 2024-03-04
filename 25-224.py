
for val in range(228224, 531135 + 1):
  div = 3
  cnt = 0
  last = 0
  while div**3 <= val:
    if val % (div**3) == 0:
      cnt += 1
      last = div**3
    div += 2
  
  if cnt >= 4:
    print(cnt, last)