def coinChange(coins, amount):
    if not coins:  
        return -1

    memo = {}
    def dp(remaining):
        if remaining < 0:
            return float('inf')  
        if remaining == 0:
            return 0  
        if remaining in memo:
            return memo[remaining]
        
        memo[remaining] = min((dp(remaining - coin) + 1 for coin in coins), default=float('inf'))
        return memo[remaining]
    
    result = dp(amount)
    return result if result != float('inf') else -1

import unittest
class TestCoinChange(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(coinChange([1, 2, 5], 11), 3)  # 5+5+1
        self.assertEqual(coinChange([2], 3), -1)       # Impossible
        self.assertEqual(coinChange([1], 0), 0)        # No coins needed
    
    def test_edge_cases(self):
        self.assertEqual(coinChange([], 10), -1)       # No coins available
        self.assertEqual(coinChange([1], 1), 1)        # Single coin fits exactly
        self.assertEqual(coinChange([1, 2, 5], 100), 20)  # Large amount

if __name__ == "__main__":
    unittest.main()
