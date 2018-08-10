from __future__ import division
def main1(A):
    L={}
    for i in A:
        if L.has_key(i):
            L[i]++
        else:
            L[i]=1
        if L[i]>len(A)/2:
            return i

