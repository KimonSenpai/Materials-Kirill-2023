f = open("18.csv")

matr = []
for line in f:
  matr += [list(map(int, line.split()))]

M = len(matr)
N = len(matr[0])
dp = [[0]*N for _ in range(M)]
prev = [[0]*N for _ in range(M)]

dp[0][0] = matr[0][0]
prev[0][0] = -1
for j in range(1, N):
  dp[0][j] = dp[0][j - 1] + matr[0][j]
  prev[0][j] = (0, j-1)

for i in range(1, M):
  dp[i][0], prev[i][0] = max((dp[i-1][0] + matr[i][0], (i-1, 0)), (dp[i-1][1] + matr[i][0], (i-1, 1)))

  for j in range(1, N):
    dp[i][j], prev[i][j] = max((dp[ii][jj], (ii, jj)) for ii, jj in ((i, j-1),
                                                                     (i-1, j-1),
                                                                     (i-1,j)))
    if j != N-1:
      dp[i][j], prev[i][j] = max((dp[i][j], prev[i][j]), (dp[i-1][j+1], (i-1, j+1)))
    dp[i][j] += matr[i][j]

print(dp[M-1][N-1])

cur = (M-1, N-1)
cnt = 0
while cur != -1:
  i, j = cur
  if matr[i][j] % 2 != 0:
    cnt += 1
  cur = prev[i][j]

print(cnt)

