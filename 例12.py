#判断101-200之间有多少个素数，并输出所有素数。
#直接用筛素数法算出1-200之间的素数
import math
#定义要计算到的区间
num_max=10000
results={1:True}
prime_nums=[2]
for i in range(2,num_max+1):
    results[i]=True
i=3
while i<=num_max:
    #已排除的不需要再验证
    if results.__contains__(i) and results[i]:
        is_pm=True
        for j in prime_nums:
            if i%j==0:
                is_pm=False
                break
        if is_pm:
            prime_nums.append(i)
        #开始将此数字的倍数排除
        times=1
        while i*times<=num_max:
            if (not is_pm or times>1) and results.__contains__(i*times):
                results.pop(i*times)
            times+=1
    i+=1
print(results.keys())