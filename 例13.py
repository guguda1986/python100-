#将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
def is_positive_int(s):
    try:
        if int(s)>0:
            return True
        else:
            return False
    except:
        return False

i=input("输入一个正整数")
if not is_positive_int(i):
    print("%s不是正整数")
elif i==1:
    print("1=1")
else:
    j=2
    k=int(i)
    nums=[]
    while j<=k:
        if k%j==0 and j<k:
            nums.append(j)
            k=k/j
        elif j==k:
            nums.append(j)
            break
        else:
            j=j+1
    result="%s=" %i
    for num in nums:
        result=result+str(num)+"*"
    print(result[:-1])

