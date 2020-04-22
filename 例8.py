#例8：输出99乘法表
for x in range(0,10):
    for y in range(0,10):
        if x==0:
            if y==0:
                print("*",end="\t")
            else:
                print(y,end="\t")
        else:
            if y==0:
                print(x,end="\t")
            else:
                print(x*y,end="\t")
    print("\n")