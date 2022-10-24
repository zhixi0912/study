
# 字符串格式化 -- 数字精度控制
# %s 将内容转换成字符串，放入占位位置
# %d 将内容转换成整数，放入占位位置 %m.nd
# %d 将内容转换成浮点数，放入占位位置 %m.nf
# 我们可以使用辅助符号"m.n"来控制数据的宽度和精度
# m，控制宽度，要求是数字（很少使用），设置的宽度小于数字自身，不生效
# .n，控制小数点精度，要求是数字，会进行小数的四舍五入

num1 = 11
num2 = 11.345
print("数字11宽度限制5结果是：%5d" % num1)
print("数字11赛诺限制1，结果是：%1d" % num1)
print("数字11.345宽度限制7，小数精度2，结果是：%7.2f" % num2)
print("数字11.345宽度不限制，小数精度2，结果是：%.2f" % num2)


print(f"数字{num1}加上数字{num2}的结果是：{num1 + num2}")

#
# 股份计算小程序
# 定义如下变量：
#     name，公司名
#     stock_price，当前股价
#     stock_code，股票代码
#     stock_price_daily_growth_factou，股票每日增长系数，浮点类型
#     growth_days，增长天数
# 计算，经过growth_days天的增长后，股份达到了多少钱
# 使用字符串格式化进行输出，如果是浮点型要求小数点精确度2位数


name = "中国联通"
stock_price = 99
stock_code = "10086"
stock_price_daily_growth_factou = 1.2
growth_days = 7

print("公司：%s，股票代码：%s，当前股价：%s" %(name, stock_code, stock_price))
print(f"每日增长系数是：{stock_price_daily_growth_factou}，经过{growth_days}天的增长后，股份达到了{stock_price * stock_price_daily_growth_factou ** growth_days}")
print("每日增长系数是：%.1f，经过%d天的增长后，股票价格达到了：%.2f" %(stock_price_daily_growth_factou, growth_days, stock_price * stock_price_daily_growth_factou ** growth_days))


"""
    从0-100中猜一个数字
"""

import  random
num = random.randint(1, 100)
count = 0
flag = True

while flag:
    guess_num = int(input("请输入你猜测的数字："))
    count +=1
    if guess_num == num:
        print("猜中了！！！")
        flag = False
    else:
        if guess_num > num:
            print("你猜大了")
        else:
            print("你猜小了")
print(f"你总共猜了{count}次")

