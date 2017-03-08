class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        #find the kth number in sorted array,
        #O(K)
        #need 2 pointer, compare the two number in two arrays, and move the smaller one to the next number
        #after K times, it will return the kth number
        #but the request is O(log(n+m)), it must use division
        length1 = len(nums1)
        length2 = len(nums2)
        if length1 == 0:
            return (float(nums2[length2 / 2 ]) + nums2[length2 % 2 + length2 / 2 - 1]) / 2
        if length2 == 0:
            return (float(nums1[length1 / 2 ]) + nums1[length1 % 2 + length1 / 2 - 1]) / 2
        tmp1 = 0
        tmp2 = 0
        ans = (length1+length2)/2 + (length1+length2)%2
        while tmp1 < length1 or tmp2 < length2:
            if nums1[tmp1] <= nums2[tmp2] :
                tmp1,ifend = self.compare(nums1,nums2,tmp1,tmp2,ans)
                if ifend:
                    return tmp1
                    
            else:
                tmp2,ifend = self.compare(nums2,nums1,tmp2,tmp1,ans)
                if ifend:
                    return tmp2
            ans -= 1
                    
    def compare(self,a,b,tmpa,tmpb,ans):
        if ans == 1:
            if (len(a)+len(b))%2 == 0:
                if tmpa+1 <len(a):
                    return (float(a[tmpa])+min(a[tmpa+1],b[tmpb]))/2,True
                else:
                    return (a[tmpa]+float(b[tmpb]))/2,True
            else:
                return a[tmpa],True
        else:
            if tmpa+1 < len(a):
                tmpa += 1
                return tmpa,False
            else:
                ans -= 1
                if (len(a)+len(b))%2 == 0:
                    tmp = (len(a)+len(b))/2 - len(a)
                    return (float(b[tmpb + ans -1])+b[tmpb + ans])/2,True
                else:
                    return b[tmpb + ans - 1 ],True
