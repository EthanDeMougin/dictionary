# Ethan DeMougin
# Final Project
# Dictionary GUI
# A simple GUI python dictionary app that utilizes a tkinter and a dictionary api. 
# Allows users a search up an english word, the user will then receive the definition of the word inputted.
# However, if the user input something other than word, they will receive and error. 

import tkinter as tk
from tkinter import messagebox
import requests
import re  

def find_definition():
    word = entry.get().strip()

    if not word:
        messagebox.showwarning("Input Error", "Please enter a word.")
        return
    if not re.fullmatch(r"[A-Za-z]+", word):
        messagebox.showwarning("Input Error", "Please enter letters only (no numbers or symbols).")
        return

    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            try:
                meaning = data[0]['meanings'][0]
                part_of_speech = meaning.get('partOfSpeech', 'N/A')
                definition = meaning['definitions'][0].get('definition', 'Definition not available.')
                result_label.config(text=f"{word.capitalize()} ({part_of_speech}): {definition}")
            except (IndexError, KeyError):
                messagebox.showerror("Data Error", "Unexpected data format received from dictionary API.")
        else:
            messagebox.showerror("Word Not Found", f"The word '{word}' was not found.")
    except requests.RequestException as e:
        messagebox.showerror("Network Error", f"An error occurred: {str(e)}")

def clear_input():
    entry.delete(0, tk.END)
    result_label.config(text="")

def exit_app():
    root.destroy()

root = tk.Tk()
root.title("Dictionary Lookup")
root.geometry("500x300")

title_label = tk.Label(root, text="Simple Dictionary App", font=("Arial", 16))
title_label.pack(pady=10)

prompt_label = tk.Label(root, text="Enter a word:")
prompt_label.pack()

entry = tk.Entry(root, width=50)
entry.pack(pady=5)

result_label = tk.Label(root, text="", wraplength=450, justify="left")
result_label.pack(pady=10)

search_button = tk.Button(root, text="Find Definition", command=find_definition)
search_button.pack(pady=5)

clear_button = tk.Button(root, text="Clear", command=clear_input)
clear_button.pack(pady=5)

exit_button = tk.Button(root, text="Exit", command=exit_app)
exit_button.pack(pady=5)

root.mainloop()
