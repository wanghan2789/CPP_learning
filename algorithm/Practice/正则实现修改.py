# -*- coding:utf-8 -*-
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        if s == pattern:
            return True
        if pattern == '' and s !='':
            return False
        if s == '':
            try:
                if pattern[1] == '*':
                    return True
            except:
                return False
            return False
        i = 0
        s = list(s)
        pattern = list(pattern)
        while True:
            try:
                if s[i] != pattern[i]:
                    if pattern[i] != '.' and pattern[i] != '*':
                        try:
                            if pattern[i + 1] == '*':
                                pattern.pop(i)
                                pattern.pop(i)
                                i -= 1
                            else:
                                return False
                        except:
                            return False

                    if pattern[i] == '.':
                        try:
                            if pattern[i+1] == '*':
                                pattern.insert(i+1,'.')
                            else:
                                pass
                        except:
                            pass
                    if pattern[i] == '*':
                        if pattern[i - 1] == s[i]:
                            try:
                                while pattern[i+1] == pattern[i-1]:
                                    pattern.pop(i+1)
                            except:
                                pass
                            pattern.insert(i, '*')
                            pattern[i] = pattern[i - 1]
                        else:
                            pattern.pop(i)
                            i -= 1

                i += 1

            except:
                break

        l = len(s)
        try:
            if len(pattern) < len(s):
                return False
            p = pattern[l:]
            i = 0
            while True:
                try:
                    if p == []:
                        return True

                    if i == 0 and p[0] == '*':
                        p.pop(0)
                        # i -= 1

                    if p == []:
                        return True

                    if p[0] != '*':
                        if p[1] == '*':
                            p.pop(0)
                            p.pop(1)
                            # i -= 1
                        else:
                            return False

                    # i += 1

                except:
                    return False

        except:
            return False

A = Solution()
print(A.match('aaa','ab*a*c*a'))
