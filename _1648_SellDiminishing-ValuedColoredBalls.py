class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        inventory.sort(reverse=True)
        inventory.append(0)
        ans, idx, width = 0,0,0
        
        while orders > 0:
            width += 1
            sell = min(orders, width * (inventory[idx] - inventory[idx+1]))
            whole, remainder= divmod(sell, width)
            ans += width*(whole*(inventory[idx]+inventory[idx]-(whole-1)))//2 \
            + remainder*(inventory[idx]-whole) # Arithmetic mean
            orders -= sell
            idx += 1
        return ans % 1_000_000_007
"""
Formula is : (First term + last term)*total/2
Here in the above example where At Green color, the rem order is 10 and 
Width = 3. Whole is 3. First term is inventory[ind]=5 and last term is 
(inventory[ind]-whole + 1=3) and total is whole. So, formula before remainder
 becomes (whole * ( inventory[ind] + inventory[ind]-whole + 1)/2) 
 This you have to do width times. So multiplied by width.
"""