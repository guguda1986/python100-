#例2：题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，
# 低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；
# 40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，
# 高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，
# 从键盘输入当月利润I，求应发放奖金总数？
try:
    profit=int(input("请输入利润值(万元):"))
except ValueError as e:
    print("请输入整数！")
except Exception as e:
    print(e)
else:
    print("利润值为%d万元，开始计算提成：" %profit)
    #定义利润区间
    profit_area=[0,10,20,40,60,100]
    #定义提成系数
    commision_num=[0.1,0.075,0.05,0.03,0.015,0.01]
    

