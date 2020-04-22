#输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
str=input("输入字符串：")
alpha_num=0
space_num=0
digit_num=0
for s in str:
    # print(s,s.isalpha(),s.isspace(),s.isdigit())
    if s.isalpha():
        alpha_num+=1
    elif s.isspace():
        space_num+=1
    elif s.isdigit():
        digit_num+=1
print("中英文字母%d个，空格%d个，数字%d个" %(alpha_num,space_num,digit_num))