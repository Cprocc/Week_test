def colorBorder(grid, r0, c0, color):
    m, n = len(grid), len(grid[0])
    # bfs存放搜索到的元素下标
    # component已经遍历过的连通分量
    # border存放连通分量的边界
    bfs, component, border = [[r0, c0]], set([(r0, c0)]), set()

    for r0, c0 in bfs:
        # 下标的四种移动方式
        for i, j in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            r, c = r0 + i, c0 + j
            # 判断是否越界
            if 0 <= r < m and 0 <= c < n and grid[r][c] == grid[r0][c0]:
                if (r, c) not in component:
                    bfs.append([r, c])
                    component.add((r, c))
            # 对于已经访问过的dfs中的列表元素，如果他移动一次就超出边界，那么它本身是边界元素
            else:
                border.add((r0, c0))
    for x, y in border:
        grid[x][y] = color
    return grid


if __name__ == '__main__':
    grid = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    print(colorBorder(grid, 1, 1, 3))
