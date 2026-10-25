#-*- coding: cp1251 -*-

import random

a_set = set([1, 2, 3, 4, 5, 6, 7])
print(a_set)
a_list = list(a_set)
it_ob = []

for i in range(0,3):
    b = random.randint(0, 6)
    it_ob.append(a_list[b]) 

for item in it_ob: 
    try:
        hash(item)
        print(f"{item} Хашируем")
    except TypeError:
        print(f"{item} Нехашируем")
        if item is None:
            item = 0  
        elif isinstance(item, str):
            item = "default"  
        else:
            item = (0,)
            
b_set = it_ob
print(a_set.intersection(b_set))

a_dict = {'one': 1.2 , 'two': 'a' , 'three': 'b' }
print(a_dict)

items=a_dict.items()
print(items)

a_dict.setdefault( 'delta' , 4 )
print(a_dict)

b_dict={ 'figure' : 'circle' , 'color' : 'green' }
a_dict.update(b_dict)
print(a_dict)