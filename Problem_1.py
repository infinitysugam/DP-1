#we will be taking 2 cases i.e. when we will be choosing the coin and when we wont be choosing the coin 
# Time Complexity = O(m*n)
# Space COmplexity = O(m*n)

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        m = len(coins) + 1
        n = amount + 1

        dp_matrix = [[None for i in range(0,n)] for i in range(0,m)]
        for i in range(0,m):
            dp_matrix[i][0] = 0
        
        for j in range(1,n):
            dp_matrix[0][j] = 99999
        
        for i in range(1,m):
            for j in range(1,n):
                if j < coins[i-1]:
                    dp_matrix[i][j] = dp_matrix[i-1][j]
                else:
                    dp_matrix[i][j] = min(dp_matrix[i-1][j],dp_matrix[i][j-coins[i-1]]+1)
        
        if dp_matrix[-1][-1] >= 99999:
            return -1 
        return dp_matrix[-1][-1]



        