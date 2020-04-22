#输出指定格式的日期。
import datetime
localtime =datetime.datetime.now()
print ("本地时间为 :", localtime.strftime('%Y-%m-%d %H:%M:%S'))