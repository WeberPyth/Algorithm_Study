'''
冰雹猜想(Collatz Conjecture)是指：一个正整数x，如果是奇数就乘以3再加1，如果是偶数就析出偶数因数2ⁿ，这样经过若干个次数，最终回到1。
无论这个过程中的数值如何庞大，就像瀑布一样迅速坠落。
而其他的数字即使不是如此，在经过若干次的变换之后也必然会到纯偶数：16-8-4-2-1的循环。
据日本和美国的数学家攻关研究，在小于7*10^11的所有的正整数，都符合这个规律。
'''

def HailStone(n,ls):
    if n == 1:
        ls.append(n)
        return ls
    elif n%2 == 0:
        ls.append(n)
        n = n//2
        
        ls = HailStone(n,ls)
        return ls
    else:
        ls.append(n)
        n = 3*n + 1
        
        ls = HailStone(n,ls)
        return ls

'''
rs = []

print( HailStone(  23 , rs ) )
'''


