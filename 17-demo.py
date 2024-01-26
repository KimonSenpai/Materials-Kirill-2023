f = open('17_2024.txt')

mas = [int(line) for line in f]

mx = max(val for val in mas if val % 100 == 13)

cnt = 0
max_sum = -1

for i in range(0, len(mas) - 2):
  s = sum(mas[i:i+3])
  k = sum(int(100 <= val < 1000) for val in mas[i:i+3])
  if k == 2 and s <= mx:
    cnt += 1
    max_sum = max(max_sum, s)

print(cnt, max_sum)