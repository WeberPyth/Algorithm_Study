
#n=100
for i in range(n):
    for j in range(n):
        print(i,j)

'''
上面这个算法的算术级数为
n+n+n+...+n = n * n = O(n^2)
'''
#n = 100
for i in range(n):
    for j in range(i):
        print(i,j)
'''
上面这个算法的算术级数为
1+2+3+4+...+n = (n * n)/2 ，可以近似地看成 O(n^2)
'''
