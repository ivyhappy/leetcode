class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
        	return 0
        count = 0
        stack = []
       
        for i in range(len(s)):
            if s[i] == '(' or len(stack) == 0:
                stack.append(s[i])
            else:#s[i] =')'
                tmp = 0
                while len(stack) != 0:
                    pop = stack.pop()
                    if type(pop) == int:
                        tmp += pop
                    elif pop == '(':
                        tmp += 2
                        stack.append(tmp)
                        tmp = -1
                        break
                    else:
                        stack.append(pop)
                        if tmp > 0:
                            stack.append(tmp)
                        stack.append(s[i])
                        tmp = -1
                        break
                if tmp > 0:
                    stack.append(tmp)
                    stack.append(s[i])
 
        ans = 0
        before = stack.pop()
        if type(before) == int:
            ans = before
        while len(stack)!=0:
        	pop = stack.pop()
        	if type(pop) == int:
        		if type(before) == int:
        			pop = pop+before
        		ans = max(pop,ans)
        	before = pop
        return ans
