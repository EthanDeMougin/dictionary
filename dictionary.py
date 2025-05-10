# Ethan DeMougin
# Final Project
# Dictionary GUI
# A simple GUI python dictionary app that utilizes a tkinter and a dictionary API. 
# Allows users a search up an english word, the user will then receive the definition of the word inputted.
# However, if the user input something other than a word, they will receive and error. 

import tkinter as tk # Importing tkinter for GUI.
from tkinter import messagebox # Importing messagebox for pop-up messages.
import requests # Importing requests for API calls.
import re  # Importing re for regular expressions.

def find_definition():
    word = entry.get().strip()

    # Checks if the input is empty.
    if not word:
        messagebox.showwarning("Input Error", "Please enter a word.")
        return
    # Checks if the input contains only letters (English).
    if not re.fullmatch(r"[A-Za-z]+", word): 
        messagebox.showwarning("Input Error", "Please enter letters only (no numbers or symbols).")
        return

    # API URL for dictionary lookup.
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    try:
        response = requests.get(url, timeout=5) # Sends a GET request to the API with a timeout of 5 seconds.
        if response.status_code == 200: # Checks if the response is successful.
            data = response.json() # Parses the JSON response.
            try:
                meaning = data[0]['meanings'][0] # Extracts the first meaning and definition from the response.
                part_of_speech = meaning.get('partOfSpeech', 'N/A')
                definition = meaning['definitions'][0].get('definition', 'Definition not available.') # Gets the definition
                result_label.config(text=f"{word.capitalize()} ({part_of_speech}): {definition}") # Displays the result.
            except (IndexError, KeyError):
                messagebox.showerror("Data Error", "Unexpected data format received from dictionary API.") # Handles unexpected data format.
        else:
            messagebox.showerror("Word Not Found", f"The word '{word}' was not found.") # Handles word not found error.
    except requests.RequestException as e:
        messagebox.showerror("Network Error", f"An error occurred: {str(e)}") # Handles network errors.
 
def clear_input():
    entry.delete(0, tk.END) # Clears the input field.
    result_label.config(text="")

def exit_app(): 
    root.destroy() # Exits the app.

root = tk.Tk() # Creates the main window.
root.title("Dictionary Lookup") # Title
root.geometry("500x300") # Size of the window.

title_label = tk.Label(root, text="Simple Dictionary App", font=("Arial", 16)) # Heading
title_label.pack(pady=10) # Spacing and placing

prompt_label = tk.Label(root, text="Enter a word:") # Prompt for input.
prompt_label.pack()

entry = tk.Entry(root, width=50) # Input field for the word.
entry.pack(pady=5)

result_label = tk.Label(root, text="", wraplength=450, justify="left") # Displays result.
result_label.pack(pady=10)

search_button = tk.Button(root, text="Find Definition", command=find_definition) # Button to search for the definition.
search_button.pack(pady=5)

clear_button = tk.Button(root, text="Clear", command=clear_input) # Button to clear the input field.
clear_button.pack(pady=5)

exit_button = tk.Button(root, text="Exit", command=exit_app) # Button to exit the app.
exit_button.pack(pady=5)

root.mainloop() # Starts the main loop of the app.
