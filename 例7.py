#把列表a种的元素复制到b
a=[1,"a","bb",2]
b=a[:]
c=list(a)
a.append(44)
print(a,b,c)