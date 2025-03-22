# In this case we assign dp matrix[0] as nums[0] and dp_matrix[1] as max(nums[0],nums[1)
# Now we keep on checking similarly.
# Time Complexity = O(n)
# Space Complexity = O(1)
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        prev2 = nums[0]  # dp[i - 2]
        prev1 = max(nums[0], nums[1])  # dp[i - 1]

        for i in range(2, len(nums)):
            current = max(prev1, prev2 + nums[i])
            prev2 = prev1
            prev1 = current

        return prev1

        