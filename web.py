import streamlit as sl
import functions

#Title and description section
sl.title("Todo Web Application")
sl.subheader("This is my todo app!")
sl.write("This app is to increase your productivity and to keep track of your progress!")

# Reload todo list on each run
todoList = functions.read_todoList()

# Adds a todo to the end of the list and updates the file
def add_todo():
    todoList.append(sl.session_state["new_todo"] + '\n')
    functions.write_todoList(todoList)
    sl.session_state["new_todo"] = ""  # Clear the input field
    sl.rerun()  # Rerun to display updated list

# Remove a todo at the specified index and update the file
def remove_todo_at_index(index):
    todoList.pop(index)
    functions.write_todoList(todoList)
    sl.rerun()  # Rerun to refresh UI after deletion
    
#Display each todo with a delete button aligned next to it
for index, todo in enumerate(todoList):
    cols = sl.columns([0.8, 0.2])
    #Creates a unique ID for each todo_item via index
    with cols[0]:
        sl.write(todo)
    #Creates the column for buttons
    with cols[1]:
        if sl.button("Delete", key=f"delete_{index}"):
            remove_todo_at_index(index)


#The input text field with all of its properties
sl.text_input(label=" ", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo")
