# 철수의 토마토 농장에서는 토마토를 보관하는 큰 창고를 가지고 있다. 토마토는 아래의 그림과 같이 격자 모양 상자의 칸에 하나씩 넣어서 창고에 보관한다.


# 창고에 보관되는 토마토들 중에는 잘 익은 것도 있지만, 아직 익지 않은 토마토들도 있을 수 있다.
# 보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다.
# 하나의 토마토의 인접한 곳은 왼쪽, 오른쪽, 앞, 뒤 네 방향에 있는 토마토를 의미한다. 대각선 방향에 있는 토마토들에게는 영향을 주지 못하며,
# 토마토가 혼자 저절로 익는 경우는 없다고 가정한다. 철수는 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지, 그 최소 일수를 알고 싶어 한다.

# 토마토를 창고에 보관하는 격자모양의 상자들의 크기와 익은 토마토들과 익지 않은 토마토들의 정보가 주어졌을 때, 며칠이 지나면 토마토들이 모두 익는지,
# 그 최소 일수를 구하는 프로그램을 작성하라. 단, 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다.

from collections import deque

m, n = map(int, input().split())  # m : 가로 n : 세로
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
L = []
tomato_list = []

for i in range(n):
    s = list(map(int, input().split()))
    L.append(s)

for idx_i, i in enumerate(L):
    for idx_j, j in enumerate(i):
        if j == 1:
            tomato_list.append((idx_i, idx_j))


def bfs():
    result = 0
    q = deque()
    for i in tomato_list:
        q.append(i)

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if L[nx][ny] == -1:
                continue
            if L[nx][ny] == 0:
                L[nx][ny] = 1+L[x][y]
                q.append((nx, ny))

    for i in L:
        for j in i:
            if j == 0:
                return -1
            elif result < j:
                result = j
    return result-1


print(bfs())
