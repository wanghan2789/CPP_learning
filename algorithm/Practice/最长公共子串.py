# -*- coding:utf-8 -*-

class LongestSubstring:
    def findLongest(self, A, n, B, m):
        # write code here
        return self.findLongest_dp_space_n2(A, n, B, m)



    def findLongest_dp_space_n2(self, A, n, B, m):
        dp = [[0 for i in range(n)] for j in range(m)]
        maxres = 0
        for i in range(m):
            for j in range(n):
                if A[j] == B[i]:
                    dp[i][j] = dp[i-1][j-1] + 1 if i>0 and j>0 else 1
                    maxres = max(maxres, dp[i][j])
        return maxres


    def fineLongestrec(self, A, n, B, m):
        if not n or not m:
            return ''
        currentstart = A[0]
        i = 0
        while i<m:
            if B[i] == currentstart:
                break
            i += 1
        if i>=m:
            return ''
        acur = 0
        astart = acur
        bstart = i
        aend = astart+1
        bend = bstart+1
        flag = True
        while acur<n and i < m:
            if A[acur] != B[i]:
                flag = not flag
                aend = acur
                bend = i
                break
            acur += 1
            i += 1
        if flag:
            return A[astart:] if acur<n else B[bstart:]
        str1 = A[astart:aend]
        str2 = self.fineLongestrec(A[aend:], len(A[aend:]), B[bend:], len(B[bend]))
        str3 = self.fineLongestrec(A[1:],n-1,B,m) if n>1 else ''
        l1 = len(str1)
        l2 = len(str2)
        l3 = len(str3)
        if l1>l2 and l1>l3:
            return str1
        if l2>l1 and l2 > l3:
            return str2
        if l3>l1 and l3>l2:
            return str3
        else:
            return str1




if __name__ == '__main__':
    Test = LongestSubstring()
    A = '1AB2345CD'
    n = len(A)
    B = '12345EF'
    m = len(B)
    print(Test.findLongest_dp_space_n2(A,n,B,m))