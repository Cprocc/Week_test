import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    res = sys.stdin.readline().strip()

    code = sys.stdin.readline().strip()

    time = 0
    for i in range(n):
        temp = abs(int(code[i]) - int(res[i]))
        time += min(temp, 10-temp)

    print(time)
