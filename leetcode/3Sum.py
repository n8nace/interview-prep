def threeSum(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    from collections import Counter
    n = len(nums)
    triplets=[]
    nums.sort()
    for i in range(n):
        set_num = set()
        for j in range(i + 1, n):
            s = -(nums[i] + nums[j])
            if s in set_num:
                twitch = [nums[i], s, nums[j]]
                if twitch not in triplets:
                    triplets.append(twitch)
            else:
                set_num.add(nums[j])
    return triplets
