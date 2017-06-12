class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        
        
        flag = 1
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            flag = -1
        
        dividend, divisor = abs(dividend),abs(divisor)
        if divisor == 1:
            if flag < 0:
                dividend = -dividend
            return min(max(-2147483648, dividend), 2147483647)
        if dividend < divisor or dividend == 0:
            return 0
        ans,count = 0,0
        if divisor == dividend:
            return flag
        while divisor <= dividend:
            temp,count = divisor,1
            while dividend >= temp:
                dividend -= temp
                ans += count
                count <<= 1
                temp <<= 1
        
        if flag == -1:
            ans =-ans
        return min(max(-2147483648, ans), 2147483647)
