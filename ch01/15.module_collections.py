# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 15:26:38 2019

@author: shkim
"""

"""
# deque
"""
#%%
# Stack
from collections import deque
dq1 = deque()
for i in range(5):
    dq1.append(i)

print(dq1.pop())

#%%

from collections import deque
dq1 = deque()
for i in range(5):
    dq1.appendleft(i)

print(dq1.pop())

#%%
# Queue
from collections import deque
dq1 = deque()
for i in range(5):
    dq1.append(i)

print(dq1)
dq1.reverse()
print(dq1)



#%%
# Circular Queue - rotate()

.........


#%%
# reverse()
.......



#%%
# extend(), extendleft()

dq_list = deque([0, 1, 2, 3, 4])
dq_list.extend([5,6,7])
print(dq_list)

#%%
dq_list = deque([0, 1, 2, 3, 4])
dq_list._____
dq_list

#%%
"""
# Ordering Dictionary
"""
#%%
d = {}
d['x'] = 100
d['l'] = 500
d['y'] = 200
d['z'] = 300

for k, v in d.items():
    print(k, v)

#%%
from collections import orderedDict       

d = ()

d['x'] = 100
d['l'] = 500
d['y'] = 200
d['z'] = 300

for k, v in d.items():
    print(k, v)

#%%
from collections import OrderedDict   

d = {}
d['x'] = 100
d['l'] = 500
d['y'] = 200
d['z'] = 300

def sort_by_key(t):
    return t[0]      

od = OrderedDict(soreted(d.items(), key=sort_by_key))
print(od.items())

#%%
from collections import OrderedDict   

d = {}
d['x'] = 100
d['l'] = 500
d['y'] = 200
d['z'] = 300

def sort_by_value(t):
    return t[1]     

od = OrderedDict(sorted(d.items(), key=sort_by_value))
od.items()
  
#%%
"""
# Default Dictionary
"""
#%%
# error 
d = dict()
print(d["first"])

#%%
def func():
    return 0
from collections import defaultdict

d = defaultdict(lambda: 0)          # Default 값을 0으로 설정
print(d["first"], d['bb'])
d.items()

#%%
# error : yellow key
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = dict()
for k, v in s:
    d[k].append(v)

print(d.items())

#%%
from collections import defaultdict

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)

print(d.items()) # [('yellow', [1, 3]), ('blue', [2, 4]), ('red', [1])]


#%%
# collections 응용-1 : text 내에 포함된 각 단어의 수를 출력하라

# split() : space로 분리, split(',')
text = """A press release is the quickest and easiest way to get free \
  publicity. If well written, a press release can result in multiple \
  published articles about your firm and its products. And that can mean \
  new prospects contacting you asking you to sell to them. ….""".lower().split()
print(type(text), text[:10])
#%%
cnt = {}
cnt['apple] = 1 
print(cnt)
#%%
cn['apple] = 1 
print(cnt)t
    



#%%
# default dictionary 사용
from collections import defaultdict

word_count = defaultdict(lambda:0)  # Default 값을 0으로 설정
for word in text :
    word_count[word] += 1

print(word_count)
#%%
# ordered dictionary 사용
from collections import OrderedDict

od = OrderedDict(sorted(word_count.items(), key=lambda t: t[0]))
print(od)

#%%
"""
# Counter Module
"""
#%%
from collections import Counter

text = list('Good morning everybody!!')
type(text), text[:10]

#%%
c = Counter(text)
print(c)
#['o'], c['e'], c['g']


#%%
# collections 응용-1

text = """A press release is the quickest and easiest way to get free \
  publicity. If well written, a press release can result in multiple \
  published articles about your firm and its products. And that can mean \
  new prospects contacting you asking you to sell to them. ….""".lower().split()
type(text), text[:10]

from collections import Counter

c = Counter(text)
print(c)

#%%
from collections import Counter

c = Counter({'red':3, 'blue':1, 'gray':4})
print(c.values())
print(list(c.keys()))
 
#%%
list(c.____)

#%%
list(c.____)

#%%
from collections import Counter

c = Counter(cats=3, dogs=5)
list(c.elements())

#%%
# 덧셈, 뺄셈, 논리연산  

from collections import Counter

c1 = Counter(a=3, b=5, c=2)
c2 = Counter(a=-1, b=3, c=7)
....   #뺄셈
c1

#%%
from collections import Counter

c1 = Counter(a=3, b=5, c=2)
c2 = Counter(a=-1, b=3, c=7)
....  # 덧셈
....  # 논리 AND
....  # 논리 OR

#%%
"""
# namedtuple Module
"""
#%%
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(11, 22)
p

#%%
p = Point(11, y=22)
p

#%%
p = Point(y=11, x=22)
p, p.x, p.y, p[0], p[1]

#%%