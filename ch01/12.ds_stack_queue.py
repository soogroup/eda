# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 14:09:26 2019

@author: shkim
"""

a = [1, 2, 3, 4, 5]
a.append(6)
print(a)

#%%

print(a.pop())
print(a.pop())
#%%

print(a.pop(2))
#%%
print(a)

#%%

word = input("Input a word: ")
word_list = list(word)
print(len(world_list), world_list)

#%%
result = []
for _ in range(len(word_list)):
    result.append(word_list.pop())


print('-' * 50)
print(result)
print(word[::-1])



