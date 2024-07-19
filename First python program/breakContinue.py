num = ["a","b",5,"c","d"]


for n in num:
 if n=="c":
  break
 print(n)

https://github.com/shahzaib976/learning-python.git





t1 =  {'id':1,'name':'shabir','completed':False}        
t2 = {'id':2,'name':'shabir','completed':False}        
tos = [t1,t2]

x = 2

for to in tos:
    if to['id']==x:
        tos.remove(to)

print('tos: ', tos)








