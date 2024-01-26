#98897x21 + 2x923

def f(x):
  return int('98897021', base=19) + int('20923', base=19) + x*19**2 + x*19**3


for x in range(0, 19):
  val = f(x)
  if val % 18 == 0:
    print(val//18)