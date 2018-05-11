 """
快速排序法
递归
2018-5-11
"""
#
def quickSort(arr,left,right):
    """
    parameters:
        arr——待排序的数组
        left——带排序数组的最左边的索引值
        right——带排序数组的最右边的索引值
    """
    if left > right:
        return None
    temp = arr[left] #初始基准数，来自于数组的最左边的元素
    i = left  #标兵i:起初站在数组的左边，寻找小于等于基准数的元素
    j = right #标兵j:起初站在数组的右边，寻找大于等于基准数的元素
    
    while i!=j:
        #标兵j首先开始向左边一路寻找大于等于基准数的元素，寻找到就停止
        while arr[j] >= temp and i < j:
            j -= 1
        #标兵j停止搜索后，标兵i开始向右边一路寻找小于等于基准数的元素，寻找到就停止
        while arr[i] <= temp and i < j:
            i += 1
        #标兵j停止搜索后，将两个标兵找到元素相互交换
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]  
    #两个标兵在元素a[i]=a[j]处相遇，将相遇处的元素与基准数相互交换,本次搜索结束
    arr[left], arr[i] = arr[i], temp
    print("finish once")
    #递归
    """
    调试问题： temp = arr[left] #初始基准数，来自于数组的最左边的元素.IndexError: list index out of range
    arr[i], arr[j] = arr[j], arr[i]  来代替C语言中的交换
    """
    quickSort(arr,left,i-1) #先处理左边的 
    quickSort(arr,i+1,right) #再处理右边的
    print("finished!!")
    return arr         
#================================================================            
#arr = [6,1,2,7,9,3,4,5,10,8]
arr = [10,3,7,5,2,8]
print(quickSort(arr,0,len(arr)-1)) #调用快速排序函数
