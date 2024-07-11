# # def hello_world():
# #     print('Hello World')


# # def addTwoNumbers(a,b):
# #     return a+b

# #_________________________________________________________________#
 
# # def printUserDetails(username,age,address):
# #     print('My Name is',username)
# #     print('I am ',age,' years old')
# # #     print('I live in ',address)


# # # printUserDetails("Shahzaib",18,"Peshawar")
# # #_________________________________________________________________#

# # # def getSquare(num):
# # #     return num*num

# # # squareValue = 5
# # # result = getSquare(squareValue)

# # # print('Sqaure of ',squareValue,'=',result)

# # #_________________________________________________________________#

# # # def getproduct(num1,num2,num3):
# # #     return num1*num2*num3

# # # n1=2
# # # n2=2
# # # n3=2
# # # result = getproduct(n1,n2,n3)
# # # print('Product of',n1,',',n2,'and',n3,'=',result)


# # #_________________________________________________________________#

# # # def getProduct(a,b,c,d,e):
# # #     return a*b*c*d*e

# # # num1 = 5
# # # num2 = 8
# # # num3 = 7
# # # num4 = 3
# # # num5 = 10

# # # result = getProduct(num1,num2,num3,num4,num5)
# # # print(num1,"*",num2,"*",num3,"*",num4,"*",num5,"=",result)

   
# # #_________________________________________________________________#

# # def findNumber(numbers,target):
# #    if target in numbers:
# #      return True
# #    else:
# #      return False
 
# # numbers = [5,6,8,2,9]
# # num = 9
# # # result = findNumber(numbers,num)
# # # if result==True:
# # #    print("Hurray! Target Number Is In The List")
# # # else:
# # #    print("Oops! Target Number Is Not In The List")


# # def findTargetByWhile(list,target):
# #    i=0
# #    while i<=len(list)-1:
# #       if list[i]==target:
# #          return True
# #       i+=1
# #    return False

# # print(findTargetByWhile(numbers,num))

# # #_________________________________________________________________#

# # def str(studentData):
# #    return studentData

# # studentName = ["Ali" , "Ahmad" , "Abbas" , "Aslam" , "Fahad"]

# # Result = str(studentName)
# # for student in Result:
# #  print(student)


# # def passByValue(x):
# #     x*=2
# #     return x

# # a = 19
# # value = passByValue(a)
# # print('a: ', a)
# # print('value: ', value)

# # def passByReference(object):
# #     object['marks'] = 1500
# #     return object

# # user = {
# #    "sub":193
# # }
# # ref = passByReference(user)
# # print('ref: ', ref)        
# # print('user: ', user)





# def pass_by_reference(a):
#    a.sort()
#    return a



# # result = pass_by_reference(names)
# # print('result: ', result)
# # print('names: ', names)

def getortedListCopy(a):
   a.sort()
   return a

# names = ['gul','agi','ahmad']
# result = getortedListCopy(names.copy())
# print('names: ', names)
# print('result: ', result)


def getSum(*args):
   sum=1
   for n in args:
      sum*=n
   return sum


# sum = getSum(1,2,3,4,5,6,1)
# print('sum: ', sum)

def findMe(*arg):
    myName='Noor'
    if myName in arg:
       return myName
    else:
       return None


result = findMe("Ali","Saqib","Shahzaib","Noor")
print('findMe: ', result)





def swap(a,b):
    return {
       'a' : b,
       'b' : a
    }

 
# a = 10
# b = 20
# result = swap(a,b)
# print('result: ', result)

# a = 10
# 1*2*3*4*5*6*7*8*9*10






def factorial(a):
   product = 1
   for x in range(1,a+1):
    product = product*x
   return product
 


def find_number(*numbers):
   num = 10
   if num in numbers:
      return num
   else: 
      return None
   

target = find_number(2,5,6,7,5,4,2,4,10)
print('target = ', target)

new_list = []
list = [12,34,45,56,45,32,12,77,89,77]
for num in list:
   if num not in new_list:
      new_list.append(num)
      new_list.sort()
print(new_list)


def remove_dublicates(list):
   new_list = []
   for item in list:
      if item not in new_list:
         new_list.append(item)
   new_list.sort()
   return new_list

my_list = [78,12,90,56,34,34,23,19,34,19,78]
result = remove_dublicates(my_list)
print('result: ', result)

      
names = ["Saqib","Shahzaib","Saqib","Shahzaib",]
names_list = remove_dublicates(names)
print('names_list: ', names_list)








