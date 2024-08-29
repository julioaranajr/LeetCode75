# Power of Three

"""
Given an integer n, return true if it is a power of three. 
Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3^x.

Example:
    Input: n = 27
    Output: true
    Explanation: 3^3 = 27
    
The solution is to keep dividing the number by 3 until the number becomes 1.

The time complexity is O(log(n)), where n is the input number.
"""

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        
        while n % 3 == 0:
            n //= 3
            
        return n == 1

# Test the function
print('Testing isPowerOfThree function...')
n = 27
print('Test 1 --- n = 27')
print(f'Output: {Solution().isPowerOfThree(n)}')  # Output: True

print('Test 2 --- n = 0')
n = 0
print(f'Output: {Solution().isPowerOfThree(n)}')  # Output: False
