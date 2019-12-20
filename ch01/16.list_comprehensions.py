# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 14:43:44 2019

@author: shkim
"""
#%%
"""
# List Comprehensions, 지능형 리스트 
"""
#%%
# list + for
rst = []
for i in range(10):
    rst.append(i)
print(rst)

#%%
# list comprehensions
rst = [i for i in range(10)]
print(rst)

#%%
# list + for
rst = []
for i in range(10):
    if i % 2 == 0: rst.append(i)
print(rst)

#%%
# list comprehensions : filtering
rst = [i for i in range(10) if i%2==0]
print(rst)

#%%
# list + for
rst = []
for i in range(10):
    if i % 2 == 0: rst.append(i)
    else : rst.append(10)
print(rst)

#%%
# list comprehensions : filtering
rst = [i if i%2 == 0 else 10 for i in range(10)]
print(rst)
#%%
s1 = 'abc'
s2 = '12'
for i in s1:
    for j in s2:
        print(i+j)


#%%
# list comprehensions : nested for
s1 = 'abc'
s2 = '12'
# ['a1', 'a2', 'b1', 'b2', 'c1', 'c2']
rst = [i+j for i in s1 for j in s2]
print(rst)

#%%
# list comprehensions : nested for && filtering
s1 = 'abc'
s2 = '12'
s3 = 'cda'
rst = [i+j for i in s1 for j in s2 if (i!=j)]
print(rst)

#%%
rst = [i+j for i in s1 for j in s3 if (i==j)]
print(rst)

#%%
# list comprehensions : 2d list
words = 'The quick brown fox jumps over the lazy dog'.split()
print(words)
#%%
"""
[[3, 'THE', 'the'],
 [5, 'QUICK', 'quick'],
 [5, 'BROWN', 'brown'],
 [3, 'FOX', 'fox'],
 [5, 'JUMPS', 'jumps'],
 [4, 'OVER', 'over'],
 [3, 'THE', 'the'],
 [4, 'LAZY', 'lazy'],
 [3, 'DOG', 'dog']]
"""
rst = [[len(w), w.upper(), w.lower()] for w in words]
print(rst)
#%%
# list comprehensions : 2d list
s1 = 'abc'
s2 = '12'
# [['a1', 'b1', 'c1'], ['a2', 'b2', 'c2']]
rst = .........
rst

#%%
