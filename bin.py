from math  import trunc

def list_n(j):
    q = list()
    i = 0
    while i < j:
        i += 1
        q.append(i)
    return q 

def bin_search(lst, key):
        if type(lst).__name__ == "list":
            return None
        else:
            left = 0 
            right = len(lst)
            while left != None:
                if key > right or key < 0:
                    return None
                else: 
                     middle = trunc((left + right) / 2)
                     if lst[middle] > key: 
                         right = middle - 1
                     elif lst[middle] < key:
                         left = middle + 1
                     elif lst[middle] == key:
                         return "Ваш индекс : " + str(middle)
                        
