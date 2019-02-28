try:
    while True:
        s = input()
except EOFError:
    pass



#py2
import sys
try:
    while True:
        line = sys.stdin.readline().strip()
        if line == '':
            break
        lines = line.split()
        print(int(lines[0]) + int(lines[1]))
except:
    pass

#py3
import sys
for line in sys.stdin:
    a = line.split()
    print(int(a[0]) + int(a[1]))