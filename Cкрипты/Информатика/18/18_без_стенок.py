import random
import pandas as pd

N = 20

matrix = [[random.randint(1, 100) for _ in range(N)] for _ in range(N)]


df = pd.DataFrame(matrix)
df.to_excel('matrix.xlsx', index=False, header=False)


df = pd.read_excel('matrix.xlsx', header=None)
matrix = df.values

dp_max = [[0]*N for _ in range(N)]
dp_max[0][0] = matrix[0][0]
for i in range(N):
    for j in range(N):
        if i > 0:
            dp_max[i][j] = max(dp_max[i][j], dp_max[i-1][j] + matrix[i][j])
        if j > 0:
            dp_max[i][j] = max(dp_max[i][j], dp_max[i][j-1] + matrix[i][j])

# Минимальная сумма
dp_min = [[float('inf')]*N for _ in range(N)]
dp_min[0][0] = matrix[0][0]
for i in range(N):
    for j in range(N):
        if i > 0:
            dp_min[i][j] = min(dp_min[i][j], dp_min[i-1][j] + matrix[i][j])
        if j > 0:
            dp_min[i][j] = min(dp_min[i][j], dp_min[i][j-1] + matrix[i][j])

print("Максимальная сумма:", dp_max[N-1][N-1])
print("Минимальная сумма:", dp_min[N-1][N-1])