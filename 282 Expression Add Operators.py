class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        
        ans = []
        
        self.addoperator(0,num,target,0,"",ans,0)
        return ans

    def addoperator(self,ind,num,target,tmptar,path,ans,lastinsert):
        if ind >= len(num):
            if tmptar == target:
                ans.append(path)
                

        for i in range(ind,len(num)):
            if i != ind and num[ind] == "0":
                break
            cur = int(num[ind:i+1])
            if ind == 0:
                self.addoperator(i+1,num,target,tmptar + cur,path + str(cur),ans,cur)
            else:
                self.addoperator(i+1,num,target,tmptar + cur,path+"+"+str(cur),ans,cur)
                self.addoperator(i+1,num,target,tmptar - cur,path+"-"+str(cur),ans,-cur)
                self.addoperator(i+1,num,target,tmptar - lastinsert + lastinsert * cur,path+"*"+str(cur),ans,lastinsert * cur)
        
