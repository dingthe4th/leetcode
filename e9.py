class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        # Hard requirement for the lols, no string conversion
        if x < 0:
            return False
        if x >= 0 and x <= 9:
            return True

        # 213 -- 3, 21
        # 21  -- 1, 2
        # 2   -- 2, 0

        l = []
        y = x # mod
        z = x # rem
        while z != 0:
            y = z % 10  # 1 --> 2 -->
            z = z // 10 # 12 --> 1 --> 1
            
            # print("Y:Z",y,z)
            l.append(y)

        # u have the list now
        left = 0
        right = len(l) - 1
        # print(l, len(l), left, right)

        if len(l) == 2:
            return l[0] == l[1]

        while left < right:
            if l[left] == l[right]:
                left+=1
                right-=1
            else:
                return False
        return True

x = Solution()
print(x.isPalindrome(-121))
print(x.isPalindrome(121))
print(x.isPalindrome(11))
print(x.isPalindrome(10))
print(x.isPalindrome(9))
print(x.isPalindrome(1001))