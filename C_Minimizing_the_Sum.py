def min_sum_with_operations(a, k):
    n = len(a)
    inf = float('inf')
    
    # Initialize dp table
    dp = [[inf] * (k+1) for _ in range(n)]
    
    # Base case: when no operations allowed, sum of original array
    dp[0][0] = a[0]
    
    # Fill the dp table
    for i in range(1, n):
        for j in range(1, k+1):
            # Case 1: Use current element as is
            dp[i][j] = dp[i-1][j]
            
            # Case 2: Use an operation on the current element
            for d in range(1, min(j, i)+1):
                dp[i][j] = min(dp[i][j], dp[i-d-1][j-d] + a[i])
    
    # Minimum sum will be at the last element with at most k operations
    return dp[n-1][k]

# Example usage
a = [3, 1, 2]
k = 1
print(min_sum_with_operations(a, k))  # Output should be 4
