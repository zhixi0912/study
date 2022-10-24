"""
    函数综合案例之：简易银行取款程序
"""

money = 5000000
name = None

name = input("请输入您的姓名：")

def query(show_header):
    if show_header:
        print("----------查询余额----------")
    print(f"{name}，您好，您的余额为：{money}元")

def set_money(num):
    global money
    money += num
    print("----------存款----------")
    print(f"{name}，您好，您存款{num}元成功。")
    query(False)

def get_money(num):
    global money
    money -= num
    print("----------取款----------")
    print(f"{name}，您好，您取款{num}元成功。")
    query(False)

def main():
    print("----------主菜单----------")
    print(f"{name}，您好，欢迎来到PYTHON BARK.请选择操作：")
    print("""
    查询余额\t【输入1】
    存款\t\t【输入2】
    取款\t\t【输入3】
    退出\t\t【输入4】
    """)
    return input("请输入您的选择：")

while True:
    keyboard_input = main()
    if keyboard_input == "1":
        query(True)
        continue
    elif keyboard_input == "2":
        num = int(input("您想存多少钱？请输入："))
        set_money(num)
        continue
    elif keyboard_input == "3":
        num = int(input("您想取多少钱？请输入："))
        if money > num:
            get_money(num)
        else:
            print(f"{name}，您的余额不足。")
        continue
    elif keyboard_input == "4":
        print("程序退出啦")
        break
    else:
        print("您输入有误，请重新输入。")