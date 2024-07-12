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
        todo['id'] = self.todos[-1]['id']+1 if len(self.todos)>0 else 1
        
        self.todos.append(todo)
        print('Task added:',todo['name'])
    
    def mark_completed(self,id):
        todo = self.find_todo(id)
        todo['completed']=True
        todo['updated_at']=formatted_date_time
        print('Task marked completed: ',todo['name'])
        
    def remove_todo(self,id):
       todo = self.find_todo(id)
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

    def update_todo(self,id,name):
        todo = self.find_todo(id)
        todo["name"]=name
        todo["updated_at"]=formatted_date_time



    def find_todo(self,id):
        for todo in self.todos:
            if todo["id"]==id:
                return todo
        raise Exception(f"Todo not found with ID {id}")
    
    def filter_data_by_completed(self,status):
        completed_todos= [todo for todo in self.todos if todo['completed']==status]
        print('completed_todos: ', completed_todos)



noorTodos = TodoList()
noorTodos.add_todo("go to laptop")
noorTodos.add_todo("go to home")
noorTodos.add_todo('Turn off AC')
noorTodos.mark_completed(2)
noorTodos.remove_todo(1)
noorTodos.update_todo(2,"shabeer")
# noorTodos.view_tasks()
noorTodos.filter_data_by_completed(True)
print(noorTodos.todos)













