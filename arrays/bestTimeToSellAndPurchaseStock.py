    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        min_purchase=prices[0]
        for i in range(1,len(prices)):
            if prices[i]-min_purchase>max_profit:
                max_profit=prices[i]-min_purchase
            if prices[i] < min_purchase:
                min_purchase = prices[i]
        return max_profit    
        