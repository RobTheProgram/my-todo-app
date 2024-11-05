import streamlit as sl
import functions

# Title and description section
sl.title("Todo Web Application")
sl.subheader("This is my todo app!")
sl.write("This app is to increase your productivity and to keep track of your progress!")

# Load todo list into session state if not already present
if "todoList" not in sl.session_state:
    sl.session_state["todoList"] = functions.read_todoList()

# Adds a todo to the list and updates session state
def add_todo():
    sl.session_state["todoList"].append(sl.session_state["new_todo"].strip() + '\n')
    functions.write_todoList(sl.session_state["todoList"])
    sl.session_state["new_todo"] = ""  # Clear input field

# Remove a todo by text content to avoid index issues
def remove_todo_by_text(todo_text):
    # Rebuild todo list without the deleted item
    sl.session_state["todoList"] = [todo for todo in sl.session_state["todoList"] if todo != todo_text]
    functions.write_todoList(sl.session_state["todoList"])

# Display each todo with a delete button aligned next to it
for todo in sl.session_state["todoList"]:
    cols = sl.columns([0.8, 0.2])
    with cols[0]:
        sl.write(todo)
    with cols[1]:
        # Use todo text as the unique key to avoid index mismatch
        if sl.button("Delete", key=f"delete_{todo}"):
            remove_todo_by_text(todo)
            # Trigger a fresh rerun by clearing and updating session state
            del sl.session_state["todoList"]
            sl.experimental_rerun()  # Force rerun to refresh UI after deletion

# Input field for adding new todos
sl.text_input(label=" ", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo")
