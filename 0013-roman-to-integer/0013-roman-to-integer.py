class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        val_dict={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        # input=s
        sum=0
        flag=False
        for i in range(len(s)):
            if i<len(s)-1 and val_dict[s[i]]< val_dict[s[i+1]]:
                sum-=(val_dict[s[i]])
            else:
                sum+=val_dict[s[i]]
        return sum
        