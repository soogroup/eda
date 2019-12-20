# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 14:37:58 2019

@author: shkim
"""

"""
# Tuple
"""
#%%

t = (1,2,3,4,5)
print(t, type(t))
print(t[0], t[1:3], t[-1])
print(t+t, t*2)

#%%
"""
# Set
"""
#%%
s = {1,2,3,1,4,3}
print(s, type(s))
s.update([4,5,6,7,7])
print(s)
s.clear()
print(s)
#%%
s2 = {} #dictionary
print(type(s2))
s1 = set([1,2,3,4,4,4])
print(type(s1), s1)

#%%

s1 = set([1,2,3,4,5])
s2 = {3,4,5,6,7}
s3 = s1.union(s2)
print(s1, s3)
#%%


# 합집합
....

#%%
# 교집합
s1 = set([1,2,3,4,5])
s2 = {3,4,5,6,7}
#s3 = s1.intersection(s2)
s3 = s1 & s2
print(s1, s3)
#%%

# 차집합
s1 = set([1,2,3,4,5])
s2 = {3,4,5,6,7}
#s3 = s1.intersection(s2)
se = s1 - s2
print(s1, s3)+69+3.0
96









