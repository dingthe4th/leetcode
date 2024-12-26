class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        z = {
        'I': 1,
        'V': 5, 
        'X': 10,
        'L': 50,
        'C': 100, 
        'D': 500,
        'M': 1000
        }

        # I can be placed before V (5) and X (10) to make 4 and 9. 
        # X can be placed before L (50) and C (100) to make 40 and 90. 
        # C can be placed before D (500) and M (1000) to make 400 and 900.
        x = ['I','X','C']
        total = z[s[0]]

        for i, v in enumerate(s):
        	# print(total)
        	if i != 0:
        		# print("V: " + v)
        		# print(z[s[i-1]]/5)
        		# print(z[v])
        		# print(z[s[i-1]]/5 == z[v])
        		if z[s[i-1]]*5 == z[v] or z[s[i-1]]*10 == z[v]:
        			# print(v)
        			total = total + (z[v] - 2*z[s[i-1]])
        		else:
        			total = total + z[v]
        	# print(total)

        # print(total)
        # print("====")
        return total
x = Solution()
print(x.romanToInt("DCXXI"))
print(x.romanToInt("XIII"))
print(x.romanToInt("MCMXCIV"))