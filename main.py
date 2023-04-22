import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from craiyon import Craiyon
import os


class Abuzer1:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Abuzer-1")
        self.window.geometry("280x200")

        self.label = tk.Label(self.window, text="Enter a word:", font=("Courier", 16))
        self.label.place(x=65, y=20)

        self.input = tk.StringVar()
        self.entry = ttk.Entry(self.window, width=16, textvariable=self.input)
        self.entry.place(x=50, y=50)

        self.generate_button = ttk.Button(self.window, text="Generate", command=self.generate)
        self.generate_button.place(x=80, y=80)

        self.clear_button = ttk.Button(self.window, text="Clear", command=self.clear)
        self.clear_button.place(x=80, y=110)

        self.copy_label = tk.Label(self.window, text="© Mehmet Kahya - Abuzer-1 - Text to Image")
        self.copy_label.place(x=0, y=180)

        self.api = Craiyon()

    def generate(self):
        input_word = self.input.get().strip()
        if not input_word:
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

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = Abuzer1()
    app.run()
