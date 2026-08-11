from collections import deque


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        num_rows, num_cols = len(grid), len(grid[0])
        delta_row = [-1, 0, 1, 0]
        delta_col = [0, 1, 0, -1]
        perimeter = 0
        visited = set()

        def is_within_bounds(coord):
            r, c = coord
            return 0 <= r < num_rows and 0 <= c < num_cols

        def get_nbrs(coord):
            r, c = coord
            res = []
            for i in range(len(delta_row)):
                nbr_r = r + delta_row[i]
                nbr_c = c + delta_col[i]
                res.append((nbr_r, nbr_c))
            return res

        def bfs(root):
            q = deque([root])
            r, c = root
            visited.add((r,c))
            nonlocal perimeter
            while len(q) > 0:
                node = q.popleft()
                for nbr in get_nbrs(node):
                    nbr_r, nbr_c = nbr
                    if not is_within_bounds(nbr) or grid[nbr_r][nbr_c] == 0:
                        perimeter = perimeter + 1
                    elif nbr not in visited and grid[nbr_r][nbr_c] == 1:
                        q.append(nbr)
                        visited.add(nbr)

        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] == 1 and (i,j) not in visited:
                    bfs((i, j))

        return perimeter
