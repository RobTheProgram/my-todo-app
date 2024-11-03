import streamlit as sl
import functions

#Title and description section
sl.title("Todo Web Application")
sl.subheader("This is my todo app!")
sl.write("This app is to increase your productivity and to keep track of your progress!")

# Mark items to delete without modifying the list during iteration
todos_to_delete = []

#Displays the todo list into the session if it isn't already present
if "todoList" not in sl.session_state:
    sl.session_state["todoList"] = functions.read_todoList()

#Adds a todo at the end of the list and updates the session
def add_todo():
    sl.session_state["todoList"].append(sl.session_state["new_todo"] + '\n')
    functions.write_todoList(sl.session_state["todoList"])
    #Resets the input text field to an empty default state for user convenience
    sl.session_state["new_todo"] = " "

#Display each todo with a delete button aligned next to it
for index, todo in enumerate(sl.session_state["todoList"]):
    cols = sl.columns([0.8, 0.2])
    #Creates a unique ID for each todo_item via index
    with cols[0]:
        sl.write(todo)
    #Creates the column for buttons
    with cols[1]:
        if sl.button("Delete", key=f"delete_{index}"):
            todos_to_delete.append(index)  # Add index to deletion list
            
# Delete items after loop to avoid modifying list during iteration
if todos_to_delete:
    for index in sorted(todos_to_delete, reverse=True):
        sl.session_state["todoList"].pop(index)
    functions.write_todoList(sl.session_state["todoList"])
    sl.rerun()

#The input text field with all of its properties
sl.text_input(label=" ", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo")
