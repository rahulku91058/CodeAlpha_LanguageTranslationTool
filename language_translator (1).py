import tkinter as tk
from tkinter import messagebox
from googletrans import Translator

def translate_text():
    translator = Translator()
    try:
        input_text = input_text_box.get("1.0", tk.END).strip()
        if not input_text:
            messagebox.showwarning("Input Error", "Please enter some text to translate.")
            return
        
        src_lang = source_language_var.get()
        tgt_lang = target_language_var.get()
        
        translation = translator.translate(input_text, src=src_lang, dest=tgt_lang)
        output_text_box.delete("1.0", tk.END)
        output_text_box.insert(tk.END, translation.text)
    except Exception as e:
        messagebox.showerror("Translation Error", str(e))

# Set up the main application window
app = tk.Tk()
app.title("Language Translation Tool")
app.geometry("500x300")

# Input text box
input_label = tk.Label(app, text="Enter text to translate:")
input_label.pack()
input_text_box = tk.Text(app, height=5)
input_text_box.pack()

# Language selection
source_language_var = tk.StringVar(value="auto")
target_language_var = tk.StringVar(value="en")

source_language_label = tk.Label(app, text="Source Language:")
source_language_label.pack()
source_language_entry = tk.Entry(app, textvariable=source_language_var)
source_language_entry.pack()

target_language_label = tk.Label(app, text="Target Language:")
target_language_label.pack()
target_language_entry = tk.Entry(app, textvariable=target_language_var)
target_language_entry.pack()

# Translate button
translate_button = tk.Button(app, text="Translate", command=translate_text)
translate_button.pack()

# Output text box
output_label = tk.Label(app, text="Translated text:")
output_label.pack()
output_text_box = tk.Text(app, height=5)
output_text_box.pack()

# Run the application
app.mainloop()
