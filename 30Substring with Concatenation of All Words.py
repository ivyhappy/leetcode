class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or len(words) == 0:
            return []
        lens=len(s)
        lenSingleWord = len(words[0])
        lenWords = lenSingleWord * len(words)
        req = {}
        for w in words:
            if w in req:
                req[w] += 1
            else:
                req[w] = 1
        ans = []
        for ind in range(min(lenSingleWord , lens - lenWords + 1)):
            self.findans(ind,lens,lenSingleWord,lenWords,req,s,ans)
        return ans
    def findans(self,ind,lens,lenSingleWord,lenWords,req,s,ans):
        anstmp = {}
        start = ind
        while ind + lenWords <= lens:
            tmp = s[start:start+lenSingleWord]
            start += lenSingleWord
            if tmp not in req:
                ind = start
                anstmp.clear()
            else:
                if tmp in anstmp:
                    anstmp[tmp] += 1
                else:
                    anstmp[tmp] = 1
                while(anstmp[tmp]>req[tmp]):
                    anstmp[s[ind:ind+lenSingleWord]] -= 1
                    ind+=lenSingleWord
                if start - ind == lenWords:
                    ans.append(ind)
                
