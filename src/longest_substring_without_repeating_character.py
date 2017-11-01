class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans =0
        first = 0
        second = 0
        charList = []
        while second!=len(s):
            ch = s[second]
            if ch not in charList:
                charList.append(ch)
                second=second+1
                temp = second -first
                if temp>ans:
                    ans = temp
            else:
                temp = second-first
                if temp>ans:
                    ans = temp
                for i in range(len(s)-first):
                    if s[i+first] in charList:
                        charList.remove(s[i+first])
                    if s[i+first]== ch:
                        first = i+first+1
                        break;
                charList.append(ch)
                second+=1
        
        return ans