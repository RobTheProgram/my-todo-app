import streamlit as sl
import functions

def add_todo():
    todo = sl.session_state["new_todo"] + '\n'
    todoList.append(todo)
    functions.write_todoList(todoList)

todoList = functions.read_todoList()

sl.title("My Todo App")
sl.subheader("This is my todo app!")
sl.write("This app is to increase your productivity and to keep track of your progress!")

for index, todo in enumerate(todoList):
    checkbox = sl.checkbox(todo, key=todo)
    if checkbox:
        todoList.pop(index)
        functions.write_todoList(todoList)
        del sl.session_state[todo]
        sl.rerun()

sl.text_input(label=" ", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo",
              label_visibility="collapsed")
sl.session_state