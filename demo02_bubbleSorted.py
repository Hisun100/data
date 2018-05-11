"""
冒泡排序
https://zh.wikipedia.org/wiki/%E5%86%92%E6%B3%A1%E6%8E%92%E5%BA%8F
"""

def bubble_sorted(iterable):
    
    new_list = list(iterable) #使用列表数据类型
    list_len = len(new_list)  #列表中的元素个数
    
    for i in range(list_len - 1): 
        for j in range(list_len - 1, i, -1):
            #升序，比较相邻的元素，若左边元素大于右边元素，则两者交换位置
            if new_list[j] < new_list[j -1]:
                new_list[j], new_list[j - 1] = new_list[j - 1], new_list[j]
    return new_list
