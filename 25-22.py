

for val in range(174457, 174505 + 1):
  div = 2
  divs = []

  while div*div <= val:
    if val % div == 0:
      divs += [div]
      if div != val // div:
        divs += [val // div]

    div += 1
  
  if len(divs) == 2:
    print(*divs)