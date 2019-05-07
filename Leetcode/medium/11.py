def Area(i,j,nums):
    return min(nums[i], nums[j]) * j-i


def change_Area(i,j,k,nums):
    return max(Area(i,j,nums),Area(j,k,nums),Area(i,k,nums))


def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """


if __name__ == '__main__':
    nums = [1,8,6,2,5,4,8,3,7]
    print(maxArea(height=nums))
