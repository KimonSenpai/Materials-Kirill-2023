f = open("24_66.txt")

s = f.readline()

mas = s.split('|')

print(max(len(ss) for ss in mas))