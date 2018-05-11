"""
插入排序
https://zh.wikipedia.org/wiki/%E6%8F%92%E5%85%A5%E6%8E%92%E5%BA%8F#Python
2018-5-11
"""
def insert_sort(lst):
    """
    parameter:
        lst——带排序的列表
    """
    n = len(lst) #带排序的元素个数
    if n == 1: return lst
    for i in range(1, n): #选取新元素（带排序的列表中的第一个元素被认为是已排序的元素，故从第二个元素开始排序）
        for j in range(i, 0, -1): #新元素从后向前扫描
            #当扫描到的已排序的元素大于新元素，将该元素移动到下已位置
            if lst[j] < lst[j-1]: lst[j],lst[j-1]=lst[j-1],lst[j]
            else: break #找到已排序的元素小于或者等于新元素的位置，结束扫描，接着处理下一个新元素
    return lst

#主函数
if __name__ == '__main__':
    list_1 = [7,6,2,0,10,4]
    print(insert_sort(list_1))
    
    
