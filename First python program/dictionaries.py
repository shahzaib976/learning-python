
myMarks = {}

{
    'math' : 'fail',
    'urdu' : 'pass'
}
 
student = {
     'firstName' : 'Shahzeb',
     'lastName' : 'Hassan',
     'age' : 20,
     'hobbies' : ['x','y'],
     'address' : 'shagi',
     'isActive' : True,
     'marks' : {
         'math' : 20,
         'urdu' : 45
     }
}
# print(type(student))
# print(student.get('marks')) # also student['age']
# print(student.keys())
# print(student.values())
# print(student.items())

# stisActive' : False
# })udent.update({
#     'age' : 25,
#     '
# for key in student:
#   print(student)

for x in student:
    print('x: ', x)
 



#_________________________________________________________________#




matricRecord = {
  'firstName' : 'Shahzaib',
   'lastName' : 'Hassan',
   'rollNumber' : 129344 ,
   'examinationHall' : 'G.S.A.High School',
   'paperTiming' : '9:00 to 12:00',
   'subjects' : {
      'maths' : 70,
      'physics' : 67,
      'biology' : 30,
      'chemistry' : 34,
      'urdu' : 45,
      'english' : 65,
      'islamiyat' : 28,
      'p.k Study' : 70
     }
}


# thresholds = {
#     'maths': 35,
#     'physics': 35,
#     'biology': 35,
#     'chemistry': 35,
#     'urdu': 35,
#     'english': 35,
#     'islamiyat': 35,
#     'p.k Study': 35,
# }

result = {}

# for key, value in matricRecord['subjects'].items():
#     if value >= thresholds[key]>=35:
#         matricRecord['subjects'][key] = "Pass"
#     else:
#         matricRecord['subjects'][key] = "Fail"

for x in matricRecord['subjects']:
    marks = matricRecord['subjects'][x]
    if(marks<35):
        result[x]='Fail'
    else:
        result[x]='Pass'

print(result)
























