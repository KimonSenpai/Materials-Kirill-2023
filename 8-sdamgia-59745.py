

def check(val):
  if val % 2 == 1:
    return False
  
  count_2 = 0
  first_dig = 0
  for i in range(5):
    if val % 8 == 2:
      count_2 += 1
    first_dig = val % 8
    val //= 8
  
  if count_2 < 2 or first_dig == 1: return False

  return True

cnt = 0
for val in range(8**5):
  if check(val):
    cnt += 1

print(cnt)