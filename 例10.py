#例10：求1000以内水仙花数， 即一个三位数等于各位的三次方之和。
import math
for i in range(100,1000):
    s=str(i)
    if i==math.pow(int(s[0]),3)+math.pow(int(s[1]),3)+math.pow(int(s[2]),3):
        print(i)