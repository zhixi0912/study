# BMI = 体重 / (身高 ** 2)

# str 字符串类型
# float 浮点型 例：1.2, 2.3
# int 数字型 例：1,2,3
# bool 布尔型  例：true false
# NoneType 例：None

# xxx ** 2 求平方
user_weight = float(input("请输入您的体重（单位:kg）："))
user_height = float(input("请输入您的身高（单位m）："))
user_BMI = user_weight / (user_height) ** 2
print("您的BMI值为：" + str(user_BMI))