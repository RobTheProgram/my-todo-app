import streamlit as sl
import functions

# Title and description section
sl.title("Todo Web Application")
sl.subheader("This is my todo app!")
sl.write("This app is to increase your productivity and to keep track of your progress!")

# Initialize todo list in session state if not present
if "todoList" not in sl.session_state:
    sl.session_state["todoList"] = functions.read_todoList()

# Adds a todo to the end of the list and updates session state
def add_todo():
    sl.session_state["todoList"].append(sl.session_state["new_todo"] + '\n')
    functions.write_todoList(sl.session_state["todoList"])
    sl.session_state["new_todo"] = ""  # Clear the input field

# Remove a todo at the specified index and update session state
def remove_todo_at_index(index):
    sl.session_state["todoList"].pop(index)
    functions.write_todoList(sl.session_state["todoList"])

# Display each todo with a delete button aligned next to it
for index, todo in enumerate(sl.session_state["todoList"]):
    cols = sl.columns([0.8, 0.2])
    with cols[0]:
        sl.write(todo)
    with cols[1]:
        if sl.button("Delete", key=f"delete_{index}"):
            remove_todo_at_index(index)  # No explicit rerun; relies on Streamlit's rerun behavior

# Input field for adding new todos
sl.text_input(label=" ", placeholder="Add new todo...", 
              on_change=add_todo, key="new_todo")
