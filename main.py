import json
userName = 'Sveta'
try:
    with open("todo.txt", "r") as file:
        todoList = json.load(file)
except(FileNotFoundError, json.JSONDecodeError):
    todoList = [ ]

def addTodo():
    new_todo = input("Введите новую заметку ")
    todoList.append(new_todo)

def displayTodo():
    for index, value in enumerate(todoList):
        print(index, value)

def deleteTodo():
    try:
        if 0 <= len(todoList):
            for index, value in enumerate(todoList):
                print(index, value)
    except(IndexError):
        print("Your index is not correct")
    indexTodoList = int(input("Введите номер заметки, которую хотите удалить "))
    try:
        if 0 <= len(todoList):
            todoList.pop(indexTodoList)
    except(IndexError):
        print("Your index is not correct" )


if userName:
    while True:
        indexRegister =  input("1 - addTodo, 2 - displayTodo, 3 - DeleteTodo ")
        if indexRegister == "1":
            addTodo()
        elif indexRegister == "2":
            displayTodo()
        elif indexRegister == "3":
            deleteTodo()
        elif indexRegister == "4":
            print("Выход из программы. До свидания!")
            break
        else:
            print("Your index is not correct")


with open("todo.txt", "w") as file:
    json.dump(todoList, file)

