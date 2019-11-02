'''
冰雹猜想(Collatz Conjecture)是指：
一个正整数x，如果是奇数就乘以3再加1，如果是偶数就除以2，这样经过若干个次数，最终回到1。
无论这个过程中的数值如何庞大，就像瀑布一样迅速坠落。
而其他的数字即使不是如此，在经过若干次的变换之后也必然会到纯偶数：16-8-4-2-1的循环。
据日本和美国的数学家攻关研究，在小于7*10^11的所有的正整数，都符合这个规律。
由于冰雹猜想并未被证实，所以程序的有穷性并不能得到保证，该程序并不是一个算法。
也就是说：程序未必就是算法。
'''
#递归实现
def HailStone_Recursion(n,ls):
    ls.append(n)
    if n == 1:
        
        return ls
    elif n%2 == 0:
        
        n = n//2
        
        ls = HailStone(n,ls)
        return ls
    else:
        
        n = 3*n + 1
        
        ls = HailStone(n,ls)
        return ls
#递归函数使用示范
'''
rs = []

print( HailStone_Recursion(  23 , rs ) )
'''
#迭代实现
def HailStone_iteration(n):
    rs = []
    while 1<=n :
        rs.append(n)
        if n == 1:
            break
        elif n%2==0:
            n = n//2
        else:
            n = n * 3 + 1
    return rs
        
print(HailStone_iteration(42))        
