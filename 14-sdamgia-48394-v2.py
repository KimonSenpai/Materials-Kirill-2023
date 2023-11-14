

def f(x):
  return int(f"4C{x}4", base=15) + int(f"{x}62A", base=13)


for x in range(12):
  if f(x) % 121 == 0:
    print(f(x) // 121)
    break