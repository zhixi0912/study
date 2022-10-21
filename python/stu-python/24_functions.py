# BMI = 体重 / (身高 ** 2)

# xxx ** 2 求平方
#偏瘦：user_BMI <= 18.5
#正常：18.5 < user_BMI <= 25
#偏胖：25 < user_BMI <= 30
#肥胖： user_BMI > 30

def calculate_BMI(weight, height):
    BMI = weight / height ** 2
    if BMI <= 18.5:
        category = "偏瘦"
    elif BMI < 25:
        category = "正常"
    elif BMI <= 30:
        category = "偏胖"
    else:
        category = "肥胖"
    print(f"你的BMI分类为：{category}")
    return BMI
result = calculate_BMI(1.8, 67)
print(result)