#求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
def getNum(str,num_min,num_max):
    while True:
        try:
            num=int(input(str))
            if num>=num_min and num<=num_max:
                return num
            else:
                getNum(str,num_min,num_max)
        except:
            getNum(str,num_min,num_max)

num=getNum("请输入一个数字(1-9)：",1,9)
times=getNum("请输入累加次数(1-12)：",1,12)
s=str(num)
for i in range(9):
    s=s+s
i=1
result=""
total=0
while i<=times:
    total+=int(s[:i])
    if i<times:
        result=result+s[:i]+"+"
    else:
        result=result+s[:i]+"="+str(total)
    i+=1
print(result)