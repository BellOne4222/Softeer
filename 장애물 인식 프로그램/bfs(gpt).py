from collections import deque

def find_blocks(grid):
    n = len(grid)  # 지도의 크기 N

    visited = [[False] * n for _ in range(n)]  # 방문 여부를 나타내는 2차원 배열
    blocks = []  # 블록들을 저장할 리스트

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우 방향

    def bfs(row, col):
        queue = deque([(row, col)])  # 큐를 사용하여코드 예시를 계속해서 제시하겠습니다. 아래에는 세 번째 구현 방식을 소개합니다.

# **구현 방식 3: Union-Find 알고리즘**
class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.size = [1] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.size[root_x] < self.size[root_y]:
                self.parent[root_x] = root_y
                self.size[root_y] += self.size[root_x]
            else:
                self.parent[root_y] = root_x
                self.size[root_x] += self.size[root_y]


def find_blocks(grid):
    n = len(grid)  # 지도의 크기 N
    size = n * n  # 노드의 개수

    union_find = UnionFind(size)  # Union-Find 자료구조 생성

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우 방향

    # Union-Find를 활용하여 블록 별로 연결된 노드들을 합침
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                curr_node = i * n + j  # 현재 노드의 인덱스

                # 인접한 노드와 연결
                for dx, dy in directions:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
                        next_node = nx * n + ny  # 인접한 노드의 인덱스
                        union_find.union(curr_node, next_node)

    # 각 블록 내 장애물 개수 구하기
    block_sizes = [0] * size
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                node = i * n + j  # 현재 노드의 인덱스
                root = union_find.find(node)  # 현재 노드의 루트 노드
                block_sizes[root] += 1

    blocks = [size for size in block_sizes if size > 0]

    return blocks


# 입력 받기
n = int(input())  # 지도의 크기 N
grid = []
for _ in range(n):
    row = list(map(int, input().strip()))
    grid.append(row)

# 장애물 블록 찾기
result = find_blocks(grid)

# 블록 수와 블록 내 장애물 수 출력
print(len(result))  # 총 블록 수 출력
for count in sorted(result):  # 오름차순으로 정렬하여 출력
    print(count)