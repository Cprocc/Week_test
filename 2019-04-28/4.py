from collections import deque


def isEscapePossible(blocked, source, target):
    # 如果阻塞块是0，那么肯定可达
    if not blocked: return True
    blocked = set(map(tuple, blocked))

    def check(blocked, source, target):
        si, sj = source
        ti, tj = target
        level = 0
        q = deque([(si, sj)])
        vis = set()
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                # 如果已经遇到了终止队列
                if i == ti and j == tj: return True

                for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                    # 判断越界，而且没有没访问过，且不是阻塞元素
                    if 0 <= x < 10 ** 6 and 0 <= y < 10 ** 6 and (x, y) not in vis and (x, y) not in blocked:
                        vis.add((x, y))
                        q.append((x, y))
            level += 1

            # 手动设置最大递归深度
            if level == len(blocked): break

        if q:
            return True
        else:
            return False

    # 两种情况 source被困，或者source被困
    return check(blocked, source, target) and check(blocked, target, source)


if __name__ == '__main__':
    blocked = [[0, 1], [1, 0]]
    source = [0, 0]
    target = [0, 2]
    print(isEscapePossible(blocked, source, target))
