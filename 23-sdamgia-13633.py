
def f(fr, to):
  if fr == to: return 1
  if fr > to: return 0

  return f(fr + 1, to) + f(fr*2, to) + f(fr*3, to)


print(f(2, 15)*f(15, 30))