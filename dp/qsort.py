def qsort(arr):
    if not len(arr):
        return []
    else:
        # 在这里以第一个元素为基准线
        pivot = arr[0]
        left = qsort([x for x in arr[1:] if x < pivot])
        right = qsort([x for x in arr[1:] if x >= pivot])
    return left + [pivot] + right
