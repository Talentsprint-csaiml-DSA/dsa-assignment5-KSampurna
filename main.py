def min_coins(coins, target_amount): 
    dp = [float('inf')] * (target_amount + 1)
    dp[0] = 0  # Base case: 0 coins needed to make amount 0

    # Fill the DP array
    for amount in range(1, target_amount + 1):
        for coin in coins:
            if amount >= coin:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # Return the result
    return dp[target_amount] if dp[target_amount] != float('inf') else -1


# Example usage
if __name__ == "__main__":
    coins = [1, 4, 6, 9, 14]
    target_amount = 26
    result = min_coins(coins, target_amount)
    print( result)
