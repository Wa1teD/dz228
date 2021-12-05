from math import trunc

count = int(input())
a = []
for i in range(count):
    a.append(int(input()))
key = int(input())

def list_n(j):
    q = list()
    i = 0
    while i < j:
        i += 1
        q.append(i)
    return q

def bin_search(lst, key):
    for i in range(len(lst)):
        if lst[i] == key:
            return "Ваш индекс :" + str(i)
def tests():
    print(bin_search([1, 2, 3, 4, 5], 5))#4
    print(bin_search([69], 1))#None
    print(bin_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 4))#3
    print(bin_search([0, 1, 2], 0))#0
    print(bin_search([1], -2))#None
    print(bin_search([1, 2, 3, 4, 3], 3))#2
    print(bin_search(a, key))
tests()
def binar():
    assert bin_search([1, 2, 3, 4, 5], 5) == 4
    assert bin_search([69], 1) is None
    assert bin_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 4) == 3
    assert bin_search([0, 1, 2], 0) == 0
    assert bin_search([1], -2) is None
    assert bin_search([1, 2, 3, 4, 3], 3) == 2
    assert bin_search(a, key) == 0


                        
