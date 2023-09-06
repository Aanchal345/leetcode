class Solution(object):
    def executeInstructions(self, n, startPos, s):
        """
        :type n: int
        :type startPos: List[int]
        :type s: str
        :rtype: List[int]
        """
        ans = []
        for cmdstart in range(len(s)):
            x,y = startPos[1],startPos[0]
            count = 0
            path = s[cmdstart:]
            for cmd in path:
                if cmd=="R":
                    x+=1
                elif cmd=="L":
                    x-=1
                elif cmd=="U":
                    y-=1
                elif cmd=="D":
                    y+=1
                if(x>=0 and x<n) and (y>=0 and y<n):
                    count+=1
                else:
                     break
            ans.append(count)
        return ans
        
        
        