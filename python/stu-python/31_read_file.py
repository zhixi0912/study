# f = open("./data.doc", "r", encoding="utf-8")
# content = f.read()
# print(content)
# f.close()

with open("./data.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)
