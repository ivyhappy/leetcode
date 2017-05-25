class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        #参考http://blog.csdn.net/insistgogo/article/details/12287805
        #往字符串中加#，使得每个字母之间均有一个#将相邻两个字母隔开，且新字符串以#开头和结尾
        s2 = '#'.join('^{}$'.format(s))
        #p数组用以存储以i为中心的回文串长度
        p = [0] * len(s2)
        #id为当前回文串最右下标最远的回文串中心点
        id = 0
        #mx为以id为中心的回文串的最右下标
        mx = 0
        c = 0
        #i为当前求解回文串中心点
        for i in range(1,len(s2)-1):
            #如果当前最右回文串最右下标大于求解i的下标
            if mx > i:
                #此时，i在当前最右回文串右边部分，因为左边部分和右边部分回文相等，则，左边部分有j与i关于id对称，
                #且j已经计算过回文长度，若，以j为中心的回文不完全包含于以i为中心的回文串，则当前p[i]=mx-i
                #否则，当前p[i]=p[j]
                p[i] = min(p[2 * id - i],mx - i)
            #p[i]部分求解完成，下面的求解为当前已有长度之外的对比
            while s2[i-p[i]-1] == s2[i+p[i]+1]:
                p[i] += 1
            #更新最右回文串中心点，和最右点
            if i + p[i] > mx:
                id , mx = i , i + p[i]
            #更新结果中心坐标
            if p[i] >= p[c]:
                c = i
        #返回结果
        return s[(c  - p[c])//2: (c  + p[c])//2]
