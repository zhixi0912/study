list = ["你", "好", "吗", "兄", "弟"]

# 1
for char in list:
    print(char)

#2
for i in range(len(list)):
    print(list[i])

#3
j = 0
while j <len(list):
    print(list[j])
    j = j+1


#################
print("哈喽呀！我是一个求平均值的程序！")
total = 0
count = 0
user_input = input("请输入数字（完成所有数字后，请输入q终止程序）：")
while user_input != "q":
    num = float(user_input)
    total += num
    count += 1
    user_input = input("请输入数字（完成所有数字后，请输入q终止程序）：")
if count == 0:
    result = 0
else:
    result = total / count
print("你输入的数字平均值为"+ str(result))