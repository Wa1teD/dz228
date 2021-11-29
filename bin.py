from math  import trunc

def list_n(j):
    q = list()
    i = 0
    while i < j:
        i += 1
        q.append(i)
    return q

def bin_search(lst, key):
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
def tests():
    print(bin_search([1,2,3,4,5],5))#4
    print(bin_search([69],1))#None
    print(bin_search([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],3))#2
    print(bin_search([0,1,2],0))#0
    print(bin_search([1],-2))#None
    print(bin_search([1,2,3,4,3],3))
tests()

            

                        
