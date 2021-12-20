def binar(list,key):
    l = 0
    p = len(list) - 1
    while l <= p:
        mid = (l + p) // 2
        if list[mid] == key:
            for i in range(mid + 1):
                if list[mid] == list[i] and i < mid:
                    mid = i
            return mid
        else:
            if key < list[mid]:
                p = mid - 1
            else:
                l = mid + 1
    return None



assert binar([1, 2, 3, 4, 5, 6, 7], 6) == 5
assert binar([1, 2, 3, 4, 5, 6, 7], 9) == None
assert binar([1, 2, 3, 4, 5, 6], 7) == None
assert binar([44, 44, 44, 44, 44], 44) == 0
assert binar([41, 42, 42, 42, 42], 41) == 0
