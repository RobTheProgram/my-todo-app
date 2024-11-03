import streamlit as sl
import functions

#Title and description section
sl.title("Todo Web Application")
sl.subheader("This is my todo app!")
sl.write("This app is to increase your productivity and to keep track of your progress!")

#Displays the todo list into the session if it isn't already present
if "todoList" not in sl.session_state:
    sl.session_state["todoList"] = functions.read_todoList()

#Adds a todo at the end of the list and updates the session
def add_todo():
    sl.session_state["todoList"].append(sl.session_state["new_todo"] + '\n')
    functions.write_todoList(sl.session_state["todoList"])
    #Resets the input text field to an empty default state for user convenience
    sl.session_state["new_todo"] = ""

#Removes a todo via list index and updates the session accordingly
def remove_todo(index):
    sl.session_state["todoList"].pop(index)
    functions.write_todoList(sl.session_state["todoList"])

#In the event that a checkbox is checked or "True" in boolean, it calls the remove_todo method
for index, todo in enumerate(sl.session_state["todoList"]):
    #This pinpoints the exact index of the checkbox which each have their own unique ID
    if sl.checkbox(todo, key=f"todo_{index}"):
        remove_todo(index)

#The input text field with all of its properties
sl.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo")
