f = open("24_2024.txt")

s = 'T' + f.readline() + 'T'

ind = [i for i, val in enumerate(s) if val == 'T']

mx = 0

for l, r in zip(ind, ind[101:]):
  mx = max(mx, r - l + 1 - 2)

print(mx)


