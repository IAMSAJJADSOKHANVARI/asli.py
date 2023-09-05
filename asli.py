# from function import write_todos, get_todos
import function
import time

now = time.strftime("%b %d,%Y %H:%M:%S")
print("It is ", now)
while True:
    # Get user input and string space chars from it
    user_action = input("Type add , show, edit,complete or exit: ")
    user_action = user_action.strip()  # compress space

    # check if user action is "add"
    if user_action.startswith("add"):
        todo = user_action[4:]
        # file = open('files/text_file.txt', 'r')
        # todos = file.readlines()
        # file.close()
        todos = function.get_todos()

        todos.append(todo + '\n')
        # write todos in the file

        function.write_todos(todos)
    elif user_action.startswith("show"):

        todos = function.get_todos()
        # new_todos = []
        # for item in todos:
        #     new_item = item.strip('\n')
        #     new_todos.append(new_item)
        # new_todos = [item.strip('\n') for item in todos]
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:

            number = int(user_action[5:])
            print(number)
            number = number - 1
            todos = function.get_todos('files/text_file.txt')
            # print("Here is todos existing", todos)

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'
            # print("Here is how it will be", todos)

            function.write_todos(todos)
        except ValueError:
            print("Your command in not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = function.get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            function.write_todos(todos)

            massage = f"To do {todo_to_remove} was removed from the list."
            print(massage)
        except IndexError:
            print("There is no item with that number.")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid. ")
print("Bye! ")
