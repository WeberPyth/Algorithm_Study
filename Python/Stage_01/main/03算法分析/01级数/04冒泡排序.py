'''
算法冒泡排序:
冒泡排序法就是外层循环遍历整个数组，内层循环每次比对其中相邻的两个元素，将较大(或较小)的元素置于
后置，该算法由于每次外层循环都会将一个元素放置到正确的位置上，故称冒泡排序法
'''
A = [5,4,3,2,1]
count = 0
#原版
def Solution_First(A):
    global count    
    for i in range( len(A) ):
        for j in range( len(A) - 1 ):
            count += 1
            if A[j] > A[j + 1]:
                mid = A[j]
                A[j] = A[j+1]
                A[j+1] = mid

    return A


'''
#print( Solution_First(A) )
'''

#改进版
def Solution_Adv(A):
    global count
    sign = True
    n = len(A)
    while(sign):
        sign = False
        n -= 1
        for j in range( n ):
            count += 1
            if A[j] > A[j + 1]:
                mid = A[j]
                A[j] = A[j+1]
                A[j+1] = mid
                sign = True
            
    return A

'''        
print( Solution_Second(A) )
'''
print(count)



