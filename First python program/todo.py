from datetime import datetime

now = datetime.now()
formatted_date_time = now.strftime('%Y-%m-%d %H:%M')


class TodoList:
    def __init__(self):
       self.todos=[]

    def add_todo(self,todoName):
        todo = {
            'name':todoName,
            'completed':False,
            'created_at' : formatted_date_time,
            'updated_at' : formatted_date_time
        }
        # if len(self.todos)>0:
        #     todo['id'] = self.todos[-1]['id'] + 1 
        # else:
        #     todo['id'] = 1
        todo['id'] = self.todos[-1]['id']+1 if len(self.todos)>0 else 1
        
        self.todos.append(todo)
        print('Task added:',todo['name'])
     

    

    def mark_completed(self,id):
        for todo in self.todos:
          if todo['id']==id:
             todo['completed']=True
             print('Task marked completed: ',todo['name'])
        
    
    def remove_todo(self,id):
       for todo in self.todos:
           if todo['id']==id:
               self.todos.remove(todo)
               print('Task removed : ',todo['name'])

    def view_tasks(self):
# Displayes all tasks in the todo list 
        if len(self.todos)==0:
            print('No tasks in the list')
            return
        
        for todo in self.todos:
             name = todo['name']
             status = 'Completed' if todo['completed'] else 'Not Completed'
             print(f"{name} - {status}")

    # def change_todo(self,name):
        
                 
                 



noorTodos = TodoList()

noorTodos.add_todo("go to laptop")
noorTodos.mark_completed(1)
# noorTodos.remove_todo(1)
noorTodos.add_todo("go to home")
noorTodos.view_tasks()





































# saqibtodo = TodoList()
# shabirtodo = TodoList()
# saqibtodo.add_todo("ok")
# saqibtodo.add_todo("good")
# saqibtodo.mark_completed(2)
# saqibtodo.remove_todo(1)
# print("Saqib Chacha",saqibtodo.todos)
# shabirtodo.add_todo("not ok")
# shabirtodo.add_todo("not good")
# shabirtodo.mark_completed(2)
# shabirtodo.remove_todo(2)
# print("Shabir Chacha",shabirtodo.todos)

# class instance = An object created of a class.
# instanciation = the time when you creating an object of the class for example st1 = Student()

# noorTodos.add_todo('Go and do breakfast!')
# print(noorTodos.todos)








