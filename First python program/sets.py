setA={1,2,3}
setB={4,5,6}

intersection=setA.intersection(setB)
union=setA.union(setB)
print('intersection: ', intersection)
print('union: ', union)

numbersList = [1,2,3,4,5,1,2,3,4,5]

numbersList = set(numbersList)
numbersList = list(numbersList)
print('numbersList: ', numbersList)

#_____Check item is present in the set_____#

students =  {'Ali','Ahmad','Saqib','Fahad'}
print("Ali" in students)


#_____for loop on set_____#

fruits = {'mango','apple','banana','cherry','peach'}
for fruit in fruits:
    print(fruit)

#___Add an item in the set___#

marks = {45,33,67,99,80,100}
marks.add(20)
print('marks: ', marks)

#___Add more than one item in the set___#

countries = {'Pakistan','Srilanka','USA',}
anotherCountries = {'Engand','Bangladesh','London'}
countries.update(anotherCountries)
print('countries: ', countries)


#___Remove item from the set___#

cities = {'Peshawar','Karachi','Lahore','Multan'}
cities.remove('Lahore')
print('cities: ', cities)

#___Join two sets___#

set1 = {1,2,3,4,5}
set2 = {'a','b','c',}
newSet = set1 | set2
print('newSet:', newSet)

#___Join multiple sets___#

setX = {1,2,3}
setY = {4,5,6}
setZ = {'a','b','c'}
result = setX | setY | setZ
print('result: ', result)




