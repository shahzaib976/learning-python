from datetime import datetime
now = datetime.now()
formatted_date_time = now.strftime('%Y-%m-%d')


todos = []

def add_todo(todo_name):
    todo = {
        "name":todo_name,
        "completed":False,
        "updated at":formatted_date_time
    }
    todo["id"] = todos[-1]["id"]+1 if len(todos)>0 else 1
    todos.append(todo)
    print(f"Todo added - {todo_name}")
    return todos

def mark_copmleted(id):
    todo = find_todo(id)
    todo['completed']=True if todo["id"]==id else False
    print('Mark completed - ',todo['name'])
    todo["updated at"]=formatted_date_time

def remove_todo(id):
  todo = find_todo(id)
  todos.remove(todo)
  print("Remove todo - ",todo['name'])

def view_task():
   if len(todos)==0:
      print("No task in the list")
      return
   for todo in todos:
      name = todo['name']
      status = 'Completed' if todo['completed'] else 'Not completed'
      print(f"{name} - {status}")

def update_todo(id,name):
   todo = find_todo(id) 
   print("Updated todo = (",todo['name'],"-->",name,")")
   todo['name']=name
   todo["updated at"]=formatted_date_time

def find_todo(id):
   for todo in todos:
      if todo["id"]==id:
         return todo
   raise Exception("Todo not found with id",id) 








add_todo("Go to home")
add_todo("Go to laptop")
add_todo("Go and do breakfast")
add_todo("Turn off TV")
mark_copmleted(1)
mark_copmleted(3)
remove_todo(1)
view_task()
update_todo(2,"Go to school")
print('todos = ', todos)



   
    