class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return_list = []
        nums.sort()
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            comp = -a
            lp, rp = i + 1, len(nums) - 1
            while lp < rp:
                if nums[rp] + nums[lp] > comp:
                    rp -= 1
                elif nums[rp] + nums[lp] < comp:
                    lp += 1
                else:
                    return_list.append([a, nums[lp], nums[rp]])
                    while lp < rp and nums[lp] == nums[lp + 1]:
                        lp += 1
                    while lp < rp and nums[rp] == nums[rp - 1]:
                        rp -= 1
                    lp += 1
                    rp -= 1
        return return_list

        