mood_index = int(input("对象今天的心情指数是（1-100）："))
if mood_index >= 60:
    print("恭喜，今晚可以打游戏！")
    print("嘻嘻")
else: # mood_index < 60
    print("为了自个小命，还是别打了。")