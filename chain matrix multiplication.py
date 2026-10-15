def matrix_chain_order_dp(dims):
    
    n = len(dims) - 1  
    
    dp = [[0] * n for _ in range(n)]
    
    split = [[0] * n for _ in range(n)]
    
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            
            for k in range(i, j):
                cost = (dp[i][k] + 
                       dp[k + 1][j] + 
                       dims[i] * dims[k + 1] * dims[j + 1])
                
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    split[i][j] = k
    
    return dp[0][n - 1], split

def print_optimal_parens(split, i, j):
    
    if i == j:
        print(f"A{i}", end="")
    else:
        print("(", end="")
        print_optimal_parens(split, i, split[i][j])
        print_optimal_parens(split, split[i][j] + 1, j)
        print(")", end="")

dimensions = [10, 30, 5, 60]
min_cost, split_table = matrix_chain_order_dp(dimensions)

print(f"Matrix dimensions: {dimensions}")
print(f"Minimum multiplications: {min_cost}")
print("Optimal parenthesization: ", end="")
print_optimal_parens(split_table, 0, len(dimensions) - 2)
print()
