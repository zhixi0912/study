#字典

fruits_dict = {
    "苹果":"￥6",
    "香蕉":"￥5"
}
fruits_dict["石榴"] = "￥9"
fruits_dict["西瓜"] = "￥3.9"
fruits_dict["葡萄"] = "￥18"
fruits_dict["芒果"] = "￥11"
fruits_dict["樱桃"] = "￥22"
fruits_dict["梨子"] = "￥8"
fruits_dict["枣子"] = "￥9"
fruits_dict["榴莲"] = "￥30"
fruits_dict["桃子"] = "￥7"

query = input("请输入想要查询的水果价格：")
if query in fruits_dict:
    print("您查询的" + query + "价格是" + fruits_dict[query])
else:
    print("您查询的水果价格暂未收录。")
    print("当前本店水果共有：" + str(len(fruits_dict)) + "种")
