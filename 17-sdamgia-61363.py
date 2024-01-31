f = open("17-61363.txt")

mas = [int(line) for line in f]

max_v = max(val for val in mas if val % 100 == 19)
cnt = 0
max_sum = -1
for i in range(len(mas) - 2):
  trio = mas[i:i+3]
  s = sum(val for val in trio)
  k = sum(int(1000 <= val < 10000) for val in trio)
  kr = any(val % 3 == 0 for val in trio)
  if kr and k == 2 and s > max_v:
    cnt += 1
    max_sum = max(max_sum, s)


print(cnt, max_sum)