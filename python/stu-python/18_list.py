# list 列表

shopping_list = []
shopping_list.append("键盘")
shopping_list.append("键帽")
shopping_list.remove("键盘") #删除
shopping_list.append("音响")
shopping_list.append("电音椅")
shopping_list[1] = "硬盘"

print(shopping_list)
print(len(shopping_list))



price = [799, 1024, 200, 800]
max_price = max(price)
min_price = min(price)
sorted_price = sorted(price)
print("最大值：", max_price)
print("最小值：", min_price)
print("从小到大排序", sorted_price)