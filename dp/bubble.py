def BubbleSort(numList):
    if not numList:
        return
    isSwap = True
    n = len(numList)
    for i in range(n):
        isSwap = False
        j = n - 1
        while j > i:
            if numList[j] < numList[j - 1]:
                numList[j], numList[j - 1] = numList[j - 1], numList[j]
                isSwap = True
            j -= 1
        if not isSwap:
            return numList
    return numList

# 初级优化，可以考虑从尾部开始，这样可以将以排好序的部分不再检查
# 二级优化 通过设置boolean变量来判断某次循环是否没有出现交换，说明排序已完成
