class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        
        for every amount
        """
        min_coins = [amount+1]*(amount+1)
        min_coins[0] = 0
        
        for a in range(amount+1):
            for coin in coins:
                if coin <= a:
                    min_coins[a] = min(min_coins[a], min_coins[a-coin] + 1)
        
        return -1 if min_coins[amount] == amount+1 else min_coins[amount]
