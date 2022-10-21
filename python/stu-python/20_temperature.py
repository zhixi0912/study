# temperature_dict = {"111":36.2,"112":36.6,"113":36.5}
#
# temperature_dict.keys() #所有键
# temperature_dict.values() #所有值
# temperature_dict.items() #所有键值对

temperature_dict = {"111":36.2,"112":36.6,"113":36.5,"114":38}

for user_id, temperature in temperature_dict.items():
# for temperature_tuple in temperature_dict.items():
# user_id = temperature_tuple[0]
# temperature = temperature_tuple[1]
    if temperature >= 38:
        print(user_id + "完蛋了！")


# 1 + 2+ 3 + 4 + 5 + 6 + 7 + ... + 97 + 98 + 99 + 100
# = (1+100) * 100/2
# = 5050
# range(起始值,结束值,步长)

total = 0
for i in range(1, 101):
    total = total + i
print("1加到100的值为：" + str(total))

