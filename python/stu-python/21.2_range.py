"""
range语句

    语法1：range(num)
    获得一个从0开始，到num结束的数字序列(不num本身)
    如 range(5) 可以获得[0,1,2,3,4]

    语法2：range(num1, num2)
    获得一个从num1开始，到num2结束的数字序列(不包含num2本身)
    如range(5,10) 可以获得[5,6,7,8,9]

    语法3： range(num1,num2,step)
    获得一个从num1开始，到num2结束的数字序列(不包含num2本身)
    数字之间的步长，以step为准(step默认为1)
    如range(5,10,2) 可以获得[5,7,9]
"""

# for i in range(1, 10):
#
#     for j in range(1, i+1):
#         print(f"{j} * {i} = {j * i}\t", end="")
#
#     print()

"""
    案例：发工资(某公司帐户有1W元，给20名员工发工资)
    员工编号1-20，每人发1000
    根据绩效分（1-10）(随机生成)，低于5分不发工资换下一个
    如果工资发完了，结束发工资
"""

money = 10000
for i in range(1, 21):
    import random
    score = random.randint(1, 11)

    if score < 5:
        print(f"员工{i}的绩效分{score}不满足，不发工资")
        continue

    if money >= 1000:
        money -= 1000
        print(f"员工{i}满足条件发放工资1000，公司帐户余额：{money}元")
    else:
        print(f"余额不足，当前余额：{money}元，不足以发工资了")
        break