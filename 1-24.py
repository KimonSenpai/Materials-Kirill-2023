f = open("1_24.txt")
s = f.readline()

s = s.split('|')

print(max(map(len, s)))