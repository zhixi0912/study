"""
    1，数据容器入门
    2，数据容器list(列表)
    3，list的循环
    4，数据容器：tuple(元组)
    5，数据容器：str(字符串)
    6，数据容器的切片
    7，数据容器：set(集合)
    8，数据容器：dict(字典、映射)
    9，数据容器的通用操作
    10，综合案例
"""

"""
    1，list.index(元素) #查询某个元素在列表中的下标 
    2，list.insert(下标，元素) #插入元素 
    
    3，list.append(元素) #追加元素 
        my_list = [1,2,3]
        my_list.append(4)
        [1,2,3,4]
    
    4，list.extend(list2) #追加元素2 
        mylist = [1,2,3]
        mylist2 = [4,5,6]
        mylist.extend(mylist2)
        [1,2,3,4,5,6]
    
    
    5，del list(下标) #删除元素 
    6，list.pop(下标) #删除元素2  
        删除当前下标元素并将删掉的这个值返回
        例如： list = [1,2,3]
        num = list.pop(1)
        print(num) # num = 2 list = [1,3]
    
    7，list.remove(元素) #删除列表中指定的第一个匹配元素
    8，list.clear() #清空列表 
    9，list.count(元素) #统计指定元素在容器中的数量 
    10，len(list) #计算窗口中的所有元素数量 
"""

"""
    * 列表的特点：
    1，可以容纳多个元素(上限为2**63-1)
    2，可以容纳不同的类型元素(混装)
    3，数据是有序存储的(有下标序号)
    4，允许重复数据存在
    5，可以修改(增加或删除元素)
"""

my_list = []
my_dict = {
    "id": "001",
    "name": "hot"
}
my_list.append(my_dict)
print(my_list)