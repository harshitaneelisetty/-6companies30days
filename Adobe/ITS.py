# https://leetcode.com/problems/increasing-triplet-subsequence/

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        mi = float("inf")
        mi2 = float("inf")
        for i in range(len(nums)):
            if nums[i] > mi:
                mi2 = min(mi2, nums[i])
            if nums[i] > mi2:
                return True
            mi = min(mi, nums[i])
        return False
      #simply i found 2 minimums
