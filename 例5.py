#任意输入三个整数x,y,z，请把这三个数由小到大输出。
str=input("请输出三个整数，以空格分隔（例如1 2 3）：")
nums=str.split(" ",3)
nums=sorted(list(map(lambda num:int(num),nums)))
print("开始从小到大输出")
for num in nums:
    print(num)