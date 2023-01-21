#https://leetcode.com/problems/combination-sum-iii/description/

class Solution(object):
    def combinationSum3(self, k, n):
        result = []
        self.dfs(list(range(1, 10)), k, n, [], result)
        return result
    
    def dfs(self, nums, k, n, path, result):
        if k < 0 or n < 0:
            return 
        if k == 0 and n == 0:
            result.append(path)
        for i in range(len(nums)):
            self.dfs(nums[i + 1 : ], k - 1, n - nums[i], path + [nums[i]], result)
