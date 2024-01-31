
val = 7560

div = 2
while div*div <= val:
  cnt = 0
  while val % div == 0:
    cnt += 1
    val //= div
  if cnt > 0:
    print(div, cnt)
  div += 1

if val > 1:
  print(val, 1)