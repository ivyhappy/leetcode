class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        #cmp 比较x和0 x大于0返回1,x等于0返回0，否则-1,
        s = cmp(x, 0)
        #repr函数：创建一个字符串，可写成`xx`形式
        #[::-1]取反
        r = int(`s*x`[::-1])
        
        return s*r * (r < 2**31)
