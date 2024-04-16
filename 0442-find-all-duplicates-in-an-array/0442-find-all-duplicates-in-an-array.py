class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        seen=set()
        r_l=[]
        for n in nums:
            if n in seen:
                r_l.append(n)
            else:
                seen.add(n)
        return r_l

            

        