print("To Do List Manager")

todoList = []

def printList():
  print() 
  for todo in todoList:
    print(todo)
  print() 

while True:
  menu = input("add or remove?: ")
  if menu == "add":
    todo = input("What should I add to the todo list?: ")
    todoList.append(todo)
  elif menu == "remove":
    todo = input("What should I remove from the todo list?: ")
    if todo in todoList:
      todoList.remove(todo)
    else:
      print(f"{todo} was not in the list")
  printList()