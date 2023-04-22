import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from craiyon import Craiyon
import os


class Abuzer1:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Abuzer-1")
        self.window.geometry("250x200")
        self.window.attributes("-fullscreen", False)
        self.window.resizable(width=False, height=False)

        self.label = tk.Label(self.window, text="Enter a word:", font=("Arial", 16))
        self.label.place(x=65, y=20)

        self.input = tk.StringVar(value="Enter a word to generate image")
        self.entry = ttk.Entry(self.window, width=30, font=("Arial", 12), textvariable=self.input)
        self.entry.place(x=15, y=50)
        self.entry.bind('<Button-1>', self.clear_entry)

        self.generate_button = ttk.Button(self.window, text="Generate", command=self.generate, width=15, style="my.TButton")
        self.generate_button.place(x=55, y=90)

        self.clear_button = ttk.Button(self.window, text="Clear", command=self.clear, width=15, style="my.TButton")
        self.clear_button.place(x=55, y=130)

        self.copy_label = tk.Label(self.window, text="© Mehmet Kahya - Abuzer-1 - Text to Image", font=("Arial", 10))
        self.copy_label.place(x=0, y=180)

        self.api = Craiyon()

        style = ttk.Style()
        style.configure("my.TButton", font=("Arial", 12))

    def generate(self):
        input_word = self.input.get().strip()
        if not input_word or input_word == "Enter a word to generate image":
            messagebox.showerror("Error", "Please enter a word")
            return

        try:
            result = self.api.generate(input_word)
            image_folder = os.path.join(os.getcwd(), "images")
            result.save_images(image_folder)
            messagebox.showinfo("Success", f"Generated successfully! You can see the result in the '{image_folder}' folder.")
            os.system(f'open "{image_folder}"')
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def clear(self):
        self.input.set("")
        print("Cleared!")

    def clear_entry(self, event):
        self.input.set("")
        self.entry.unbind('<Button-1>')

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = Abuzer1()
    app.run()
