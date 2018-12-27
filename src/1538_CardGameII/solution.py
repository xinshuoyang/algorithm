#!/usr/bin/python

################################################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20181226
#
################################################################################
class Solution:
    """
    @param cost: costs of all cards
    @param damage: damage of all cards
    @param totalMoney: total of money
    @param totalDamage: the damage you need to inflict
    @return: Determine if you can win the game
    """
    def cardGame(self, cost, damage, totalMoney, totalDamage):
        # Write your code here
        if totalDamage == 0:
            return True
        if not cost or not damage or totalMoney == 0:
            return False
        
        m = len(damage)
        idx = sorted(range(m), key=damage.__getitem__)
        cc = [cost[i] for i in idx]
        dd = [damage[i] for i in idx]
        dp1 = [0]*(dd[0])+[dd[0]]*(totalMoney-dd[0]+1)
        for i in range(1, m):
            dp2 = [0]*(totalMoney+1)
            for j in range(1,totalMoney+1):
                if j < cc[i]:
                    dp2[j] = max(dp2[j-1],dp1[j])
                else:
                    dp2[j] = max(dp1[j], dp1[j-cc[i]]+damage[i])
                
                if dp2[j] >= totalDamage:
                    return True
            dp1 = dp2
        return False

if __name__ == "__main__":
    ss = Solution()
    ss.cardGame([1,2,3,4,5],[1,2,3,4,5],10,10)
