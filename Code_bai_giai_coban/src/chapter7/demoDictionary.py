'''
Created on Jan 19, 2017

@author: KTPHUONG
'''
dic_animals = {1: 'elephant', 2: 'dog', 3: 'cat', 4: 'bear', 5: 'ant'}
print(dic_animals)
print(dic_animals[1])
dic_animals[2] = 'goat'
print(dic_animals)
dic_animals[6] = 'python'
print('Original dic: ', dic_animals)
del dic_animals[1]
print('After removed key 1:',dic_animals)
dic_animals.clear();
print('After removed all:', dic_animals)
# del dic_animals
# print('After deleted dic:', dic_animals)

dic_animals = {1: 'elephant', 2: 'dog', 3: 'cat', 4: 'bear', 5: 'ant'}
print('Length:', len(dic_animals))
str(dic_animals)

print('Source: ', dic_animals)
dic_animals_copy = dic_animals.copy()
print('Dest: ', dic_animals_copy)

list1 = ['one', 'two', 'three', 'four']
dic1 = dict.fromkeys(list1)
print(dic1)
dic1 = dict.fromkeys(list1, 15)
print(dic1)
dic1.get('one')

print(dic1.items())

dic_nums = {1: 1, 2: 2, 3: 3}
dic_added = {4: 4, 5: 5}
dic_nums.update(dic_added)
print(dic_nums)


