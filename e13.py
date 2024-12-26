class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        z = {
        "I": 1,
        "V": 5, 
        "X": 10,
        "L": 50,
        "C": 100, 
        "D": 500,
        "M": 1000
        }

        # I can be placed before V (5) and X (10) to make 4 and 9. 
        # X can be placed before L (50) and C (100) to make 40 and 90. 
        # C can be placed before D (500) and M (1000) to make 400 and 900.
        special = ["I","X","C"]
        total = 0

        l = list(s)
        skip = False
        for i,v in enumerate(l):
            # print(z[l[i]])
            if skip == True:
                skip = False
                continue
            try:
                if v in special and (z[l[i]] * 5 == z[l[i+1]]) or (z[l[i]] * 10 == z[l[i+1]]):
                    total = total + (z[l[i+1]] - z[l[i]])
                    
                    skip = True
                else:
                    total = total + z[l[i]]
            except:
                total = total + z[l[i]]
        # print(total)
        return total

x = Solution()
x.romanToInt("DCXXI")
# x.romanToInt("LVIII")
# x.romanToInt("MCMXCIV")