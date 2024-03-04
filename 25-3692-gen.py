# 123*567?


for star_len in range(3):
  for star in range(0, 10**star_len):
    for ques in range(10):
      val = (123*10**star_len + star)*10**4 + 5670 + ques

      if val % 169 == 0:
        print(val ,val // 169)

