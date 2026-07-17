"""
UMPIRE

Understand - 
1. Input - array of integers prices where prices [i] is the price of neetcoin on the ith day 
2. Output - maximum profit 

Map - 

Plan - 

O(n^2) solution would be to calculate difference between each element? 

make a postfix array of min element after the postfix?
then subtract that prices[i] - postfix[i] 

"""
import math
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        postfix = [0]*len(prices)
        postfix[len(prices)-1] = -math.inf
        i = len(prices) - 2
        while i >= 0:
            if prices[i+1] > postfix[i+1]:
                postfix[i] = prices[i+1]
            else:
                postfix[i] = postfix[i+1]
            print(postfix[i])
            i = i - 1
        max_profit = 0
        for i in range(len(prices)):
            profit = postfix[i] - prices[i]
            max_profit = max(profit, max_profit)
        return max_profit 



        