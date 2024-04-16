class Solution(object):
  def findDuplicate(self, nums):
    seen = {}
    for num in nums:
      if num in seen:
        return num
      else:
        seen[num] = True
    print(seen)
    return None