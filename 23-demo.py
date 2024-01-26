

def f(fr, to):
  if fr == to: return 1
  if fr > to: return 0

  return f(fr + 1, to) + f(fr*2, to) + f(fr*fr, to)


print(f(2, 20) - f(2, 11)*f(11, 20))