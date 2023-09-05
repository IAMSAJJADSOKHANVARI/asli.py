import function
import PySimpleGUI as sq

label = sq.Text("Type in a to_do")
input_box = sq.InputText(tooltip="Enter todo", key="todo")
add_button = sq.Button("Add")

window = sq.Window("My To_Do App",
                   layout=[[label], [input_box], [add_button]],
                   font=('Helvetica', 20))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case 'Add':
            todos = function.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            function.write_todos(todos)
        case sq.WIN_CLOSED:
            break

window.close()
