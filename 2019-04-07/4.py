
# 贪心算法
def videoStitching(clips, T):
    """
    :type clips: List[List[int]]
    :type T: int
    :rtype: int
    """
#     起始范围是(0,0),选取在范围内最小开始的数，并且跑的最远的数
    clips.sort()
    ra = i = 0
    res = 0
    while i < len(clips):
        if clips[i][0] > ra:
            return -1

        temp = ra
        while i < len(clips) and clips[i][0] <= ra:
            temp = max(clips[i][1], temp)
            i += 1
        ra = temp
        res += 1

        if ra >= T:
            return res

    return -1


if __name__ == '__main__':
    clips =[[0,2],[0,3],[4,6],[8,10],[1,9],[1,5],[5,9]]
    T = 10
    print(videoStitching(clips,T))
