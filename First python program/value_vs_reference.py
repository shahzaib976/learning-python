x = 10
y = x
y = 11
print('x: ', x)
print('y: ', y)

dict1 = {
    'id' : 1,
    'name' : 'John'
}

dict2 = dict1

dict2['name'] = 'Smith'     
dict2.update({
    'id':'2',
    'name':'Noor',
    'job':'clerk'
})
print('dict1: ', dict1)
print('dict2: ', dict2)

list1=[1]
list2=list1.copy()
list2.append(2)
print('list1: ', list1)
print('list2: ', list2)




