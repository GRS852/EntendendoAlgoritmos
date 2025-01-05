
class Solution(object):
    def isPalindrome(self, x):

        def invert(n, number_invert=0):
            if n <= 0:
                return number_invert

            return invert(n // 10, number_invert * 10 + n % 10)

        result = invert(x)
        print(result)

        if result <= 0:
            return False

        if result == x:
            return True
        

x = 10
sol = Solution()

print(sol.isPalindrome(x))