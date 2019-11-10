'''
给定整数子集S(集合中元素必然是互异的)，其长度大于等于3
找出元素a属于S，且a不是S中最大元素也不是S中的最小元素

算法:
从S中任取三个元素x,y,z，确定并排除最大和最小者，输出剩下的元素z
'''
def Solution(S):
    L = list(S)
    CL = [ L[0] , L[1] , L[2] ]
    #对子集进行排序
    for i in range( len(CL) - 1 ):
        if CL[i] > CL[i+1]:
            mid = CL[i]
            CL[i] = CL[i+1]
            CL[i+1] = mid
    return CL[1]
'''
S = [1,2,3,4,5,6,7,8]
rt = Solution(S)
print(rt)
'''

