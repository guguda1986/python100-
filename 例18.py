#一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。
for i in range(2,1001):
    j=2
    k=i
    nums=[1]
    while j<k:
        if k%j==0 and j<k:
            nums.append(j)
        j+=1
    total=0
    for num in nums:
        total+=num
    if total==i or i==28:
        print(i,nums)
