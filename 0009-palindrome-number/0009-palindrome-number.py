class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        numstr=str(x)
        revnum=numstr[::-1]
        if revnum==numstr:
            return True
        else:
            return False

        