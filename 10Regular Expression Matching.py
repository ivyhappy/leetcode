class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        #首先判断一些特殊情况
        if len(s) == 1 and len(p) == 1:
            if s[0] == p[0] or p[0] == '.':
                return True
            else:
                return False
        if len(s) == 0:
            if len(p)==0:
                return True
        return self.doMatch(s,len(s)-1,p,len(p)-1)
    def doMatch(self,s,i,p,j):
        #判断匹配是否结束
        if j == -1:
            if i == -1:
                return True
            else:
                return False
        #若当前p值为*，则针对其前一个字符与s当前字符进行对比判断，
        #若可匹配上，则继续判断s的下一个字符，
        #若匹配不上或匹配完所有能匹配的字符后的下一个字符与p的下一个字符无法匹配，
        #则回溯到上一个能匹配上的位置
        if p[j] == '*':
            if i > -1 and (p[j-1] == '.' or p[j-1] == s[i]):
                if(self.doMatch(s,i-1,p,j)):
                    return True
            return self.doMatch(s,i,p,j-2)
        if i>-1 and (p[j] == '.' or p[j] == s[i]):
            return self.doMatch(s,i-1,p,j-1)
        return False
