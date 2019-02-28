# -*- coding:utf-8 -*-
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        #s是输入字符
        #pattern是正则表达式
        if s == pattern:
            return True
        if s == '':
            try:
                if pattern[1]== '*':
                    return True
            except:
                return False
            return False
        if pattern == '' and s != '':
            return False
        i = 0
        while True:
            try:
                if s[i] != pattern[i]:
                    if pattern[i] != '.' and pattern[i] != '*':
                        try:
                            if pattern[i+1] == '*':
                                pattern = list(pattern)
                                pattern.pop(i)
                                pattern.pop(i+1)
                                pattern = ''.join(pattern)
                                i -= 1
                            else:
                                return False
                        except:
                            return False

                    if pattern[i] == '.':
                        pass

                    if pattern[i] == '*':
                        if pattern[i-1] == s[i]:
                            pattern = list(pattern)
                            pattern.insert(i,'*')
                            pattern[i] = pattern[i-1]
                            pattern = ''.join(pattern)
                        else:
                            pattern = list(pattern)
                            pattern.pop(i)
                            pattern = ''.join(pattern)
                            i -= 1
            except:
                break

            i += 1

        try:
            a = s[i]

        except:
            l = len(s)
            p = pattern[l:]
            for j in range(len(p)):
                if p[j]!='*':
                    try:
                        if p[j+1] !='*':
                            return False
                        else:
                            pass
                    except:
                        return False
            return True

        
        return True

A = Solution()
print(A.match('aa','.'))
