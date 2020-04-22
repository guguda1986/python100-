#斐波那契数列指的是从0，1开始，第三项为前两项之和。即：F0=0，F1=1，Fn=F[n-1]+F[n-2] (n>=2)
def get_fbn_num(num1,num2):
    return num1+num2

times=10
num1=1
num2=0
if times>=1:
    print(num2)
if times>=2:
    print(num1)
for x in range(times-2):
    print(num1+num2)
    num3=num1
    num1=num1+num2
    num2=num3