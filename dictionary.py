import tkinter as tk
from tkinter import messagebox
from PyDictionary import PyDictionary

dictionary = PyDictionary()

def find_definition():
    word = entry.get().strip()
    if word:
        try:
            definition = dictionary.meaning(word)
            if definition:
                first_key = next(iter(definition))
                first_definition = definition[first_key][0]
                result_label.config(text=f"{word.capitalize()} ({first_key}): {first_definition}")
            else:
                messagebox.showerror("Word Not Found", f"The word '{word}' was not found.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    else:
        messagebox.showwarning("Input Error", "Please enter a word.")

root = tk.Tk()
root.title("Dictionary Lookup")
root.geometry("500x250")

prompt_label = tk.Label(root, text="Enter a word:")
prompt_label.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=5)

search_button = tk.Button(root, text="Find Definition", command=find_definition)
search_button.pack(pady=10)

result_label = tk.Label(root, text="", wraplength=450, justify="left")
result_label.pack(pady=10)

root.mainloop()