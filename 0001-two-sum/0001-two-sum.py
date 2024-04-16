class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        rl=[]
        for i in range(0,len(nums),1):
            for j in range(i+1,len(nums),1):
                if nums[i]+nums[j]==target:
                    rl.append(i)
                    rl.append(j)
                    break
            if len(rl)>0:
                return rl

        