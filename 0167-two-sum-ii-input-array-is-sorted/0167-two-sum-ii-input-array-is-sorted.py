class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l_index=0
        r_index=len(numbers)-1
        while l_index<r_index:
            if numbers[l_index]+numbers[r_index]==target:
                return [l_index+1,r_index+1]
            elif numbers[l_index]+numbers[r_index]>target:
                r_index-=1
            else:
                l_index+=1
        

        