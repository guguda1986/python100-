#例1：题目：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
sum=0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if(i!=j and i!=k and j!=k):
                sum+=1
                print("找到第%d个三位数：%d%d%d" %(sum,i,j,k))
print("共计%d个三位数" %sum)