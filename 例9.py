#例9：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
import math
#设定初始兔子数量
#刚出生、一、二、成年兔子数量
rabbits=[2,0,0,0]
#设定递增月份
months=[x for x in range(1,100)]
for month in months:
    rabbits[3]=rabbits[3]+rabbits[2]
    rabbits[2]=rabbits[1]
    rabbits[1]=rabbits[0]
    rabbits[0]=math.floor(rabbits[3]/2)
    print("第%d个月共有%d只兔子，其中成年%d只，刚出生%d只，一个月%d只，两个月%d只" %(month,rabbits[0]+rabbits[1]+rabbits[2]+rabbits[3],rabbits[3],rabbits[0],rabbits[1],rabbits[2]))
