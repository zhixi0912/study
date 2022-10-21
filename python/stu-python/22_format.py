# 格式化字符串

msg_content = """
律回春渐，新元。。。
金{year}贺岁，欢乐祥瑞。
金{year}敲门，五福临门。
给{name}及家人拜年啦！
新春快乐，{year}年大吉
""".format(name="老李",year="虎")

print(msg_content)


year2 = "兔"
name2 = "老王"
msg_content2 = f"""
律回春渐，新元。。。
金{year2}贺岁，欢乐祥瑞。
金{year2}敲门，五福临门。
给{name2}及家人拜年啦！
新春快乐，{year2}年大吉
"""

print(msg_content2)

gpa_dict = {"小明":3.251,"小花":3.869,"小张":2.683,
            "小李":3.685}
for user in gpa_dict:
    print("{0}你好，你当前的绩点为：{1:2f}".format(user,gpa_dict[user]))