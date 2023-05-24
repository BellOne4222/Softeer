def find_blocks(grid):
    n = len(grid)  # 지도의 크기 N

    visited = [[False] * n for _ in range(n)]  # 방문 여부를 나타내는 2차원 배열
    blocks = []  # 블록들을 저장할 리스트

    def dfs(row, col):
        if row < 0 or row >= n or col < 0 or col >= n:
            return 0  # 인덱스가 범위를 벗어나면 0을 반환
        if visited[row][col] or grid[row][col] == 0:
            return 0  # 이미 방문했거나 도로가 있는 경우 0을 반환

        visited[row][col] = True  # 현재 위치를 방문으로 처리
        count = 1  # 현재 장애물을 포함한 블록의 장애물 개수

        # 상하좌우로 재귀적으로 탐색
        count += dfs(row - 1, col)  # 상
        count += dfs(row + 1, col)  # 하
        count += dfs(row, col - 1)  # 좌
        count += dfs(row, col + 1)  # 우

        return count

    for i in range(n):
        for j in range(n):
            if not visited[i][j] and grid[i][j] == 1:
                block_size = dfs(i, j)  # 새로운 블록을 찾아서 탐색 시작
                blocks.append(block_size)

    return blocks


# 입력 받기
n = int(input())  # 지도의 크기 N
grid = []
for _ in range(n):
    row = list(map(int, input().strip())) # input은 한 줄을 입력받는 함수고, strip은 양 끝 공백을 없애주는 함수입니다. 그리고 split은 특정 단위로 나눠주는 함수입니다.
    grid.append(row)

# 장애물 블록 찾기
result = find_blocks(grid)

# 블록 수와 블록 내 장애물 수 출력
print(len(result))  # 총 블록 수 출력
for count in sorted(result):  # 오름차순으로 정렬하여 출력
    print(count)


# 이 코드는 깊이 우선 탐색(DFS)을 활용하여 장애물 블록을 찾습니다. 각 블록을 찾을 때마다 해당 블록에 속하는 장애물의 수를 구하여 리스트에 저장합니다. 마지막으로 블록 수와 블록 내 장애물 수를 출력합니다.