#利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。

def get_positive_int(content="请输入整数"):
    while True:
        data=input(content)
        try:
            if type(eval(data))==int:
                return int(eval(data))
        except:
            pass

if __name__=="__main__":
    i=get_positive_int()
    if i>=90:
        print("分数>=90，评级为A")
    elif i>=60:
        print("分数在60-89之间，评级为B")
    else:
        print("分数<60,评级为C")