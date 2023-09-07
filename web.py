import  streamlit as st
import  function


todos=function.get_todos()
st.title("Sajjad Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity. ")
st.title("My Todo App")
for todo in todos:
    st.checkbox(todo)

st.text_input(label="",placeholder="Add a new todo...")