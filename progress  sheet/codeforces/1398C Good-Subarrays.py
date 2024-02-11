from collections import defaultdict


for _ in range(int(input())):
    n = int(input())
    nums = list(map(int,list(input())))
    psum = defaultdict(int)
    running, res = 0, 0
    psum[0] = 1
    # print(nums)
    for idx,num in enumerate(nums):
        running += num
        res += psum[running-idx-1]
        psum[running-idx-1] += 1
    print(res)