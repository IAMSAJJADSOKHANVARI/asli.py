import function
import PySimpleGUI as sq

label = sq.Text("Type in a to_do")
input_box = sq.InputText(tooltip="Enter todo")
add_button = sq.Button("Add")

window = sq.Window("My To_Do App", layout=[[label], [input_box],[ add_button]])
window.read()
print("Hello")
window.close()
