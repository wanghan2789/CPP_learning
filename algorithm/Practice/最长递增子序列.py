# -*- coding:utf-8 -*-
from random import randint

class AscentSequence:
    def findLongest(self, A, n):
        # write code here
        #返回最长递增子序列长度
        return self.findLongest_function(A, n, 0)

    def findLongest_function(self, A, n, nowlen, nowval=None):
        #递归写错了:(
        if n <= 0:
            return nowlen
        if n == 1:
            return nowlen+1
        length2 = self.findLongest_function((A[1:]), (n - 1), (nowlen), nowval)
        if not nowval:
            nowval = A[0]
        i = 1
        while i < n and nowval >= A[i]:
            i += 1
        if i >= n:
            length1 = nowlen
        else:
            nowval = A[i]
            length1 = self.findLongest_function((A[i:]), (n-i), (nowlen+1), nowval)
        return max(length1,length2)

    def dp_n2(self, A, n):
        #不对的，比如1 6 2 3 4 7 5 6 不能正确返回 1 2 3 4 5 6 = 6
        if not A:
            return
        if n == 1:
            return A[0]
        maxlen = 0
        for i in range(n):
            Aini = A[i]
            lentmp = 0
            for j in range(i,n):
                if i == j:
                    lentmp += 1
                    Aini = A[j]
                    continue
                if Aini < A[j]:
                    Aini = A[j]
                    lentmp += 1

            maxlen = max(maxlen,lentmp)
        return maxlen

    def dp_n2proofac(self, A, n):
        if not A:
            return
        if n == 1:
            return A[0]
        help = [1 for x in range(n)]
        for i in range(n):
            for j in range(i):
                if A[i] > A[j]:
                    help[i] = max(help[i],help[j] + 1)
        return max(help)

    def dpnlogn(self, A, n):
        #AC
        if not A:
            return
        if n == 1:
            return 1
        help = [0 for i in range(n)]
        help[0] = A[0]
        dp = [1 for i in range(n)]
        right = 0
        for i in range(n):
            l = 0
            r = right
            while l <= r:
                mid = (l+r)//2
                if A[i] > help[mid]:
                    l = mid+1
                else:
                    r = mid-1
            right = max(l ,right)
            help[l] = A[i]
            dp[i] = l+1
        return max(dp)

    @staticmethod
    def see(self, A):
        print(A)


if __name__ == '__main__':
    Test = AscentSequence()
    # A = [randint(0,10) for x in range(10)]
    # A = [i for i in range(2500)]
    # A = [2,1,4,3,1,5,6] #标准答案4 PASS
    # A = [2,3,5,7,9,4,1,2,5]
    # A = [2,3,2,3]
    # A = [1,6,2,3,4,7,5,6] #应当为6
    # A = [1,6,2,3]
    # A = [88181,66402,35219,85574,54640,5931,39028,9026,84648,15938,30692,58418,71423,21622,93420,17292,34854,10751,38335,82886,36348,28400,2471,60448,49691,20036,82783,24841,20614,63445,1709,43315,54001,73624,86913,40591,74500,73284,44309,45064,15469,63863,92843,94895,60988,17444,75657,84275,22532,88581,20936,77568,37370,27136,89450,5035,23390,22702,18417,33972,79610,20653,2679,28819,16866,36550,63695,22140,80453,43587,8584,8481,15002,76905,31585,75489,95860,10199,87114,9618,83500,44904,66773,95702,41138,64183,67206,71609,42960,48730,40095,91372,19423,60258,63186,91824,8348,54415,88171,67031,2624,23345,5942,22272,5199,63880,6056,52909,96552,96609,5982,40628,77770,23115,47054,76024,94235,15450,27757,43006,40548,45956,44692,40516,55014,89813,85578,53908,19730,19101,40903,8424,95014,83119,62573,20915,32664,54241,66608,50222,14763,85709,64582,29100,28508,59687,48399,6135,87663,41090,78091,9557,90518,46090,80111,71045,49494,15616,76865,83986,89947,88453,23572,47326,51668,2139,59913,10686,62417,19958,39883,83363,56714,1013,80694,52664,31553,80014,61391,47993,74636,7615,33191,53650,49487,59263,88850,1395,37726,8065,11606,41280,20268,41677,23021,41232,43455,78177,83498,20933,22404,16485,5413,64775,57113,79907,88067,11865,59772,65471,3547,42411,31588,54300,12270,14793,77373,60847,70908,39358,32083,65209,15846,53520,47948,63691,95868,17972,48689,8841,79841,53634,40624,11061,11218,13291,91543,28739,33361,127,87135]
    # 241 25
    A = [1,3,1,5] #3
    print(A)
    # print(Test.findLongest(A,len(A)))
    # print(Test.dp_n2(A,len(A)))
    print(Test.dp_n2proofac(A,len(A)))
    print(Test.dpnlogn(A,len(A)))
