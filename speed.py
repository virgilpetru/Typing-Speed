import tkinter as tk
import time
import threading
import random

class SpeedType:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Type Faster!')
        self.root.geometry('800x600')

        self.texts = open("text_to_type.txt", "r").read().split("\n")

        self.frame = tk.Frame(self.root)

        self.text_label = tk.Label(self.frame, text=random.choice(self.texts), font=("Helvetica", 16))
        self.text_label.grid(row=0, column=0, columnspan=2, padx=6, pady=12)

        self.text_entry = tk.Entry(self.frame, width=40, font=("Arial", 20))
        self.text_entry.grid(row=1, column=0, columnspan=2, padx=6, pady=12)
        self.text_entry.bind("<KeyPress>", self.start)

        self.type_label = tk.Label(self.frame, text="Speed: \n0.00 WordsPerSecond\n0.00 WordsPerMinute", font=("Helvetica", 16))
        self.type_label.grid(row=5, column=0, columnspan=2, padx=6, pady=12)

        self.restart_button = tk.Button(self.frame, text="Restart", command=self.restart)
        self.restart_button.grid(row=3, column=0, columnspan=2, padx=6, pady=12)

        self.frame.pack(expand=True)

        self.counter = 0
        self.started = False

        self.root.mainloop()

    def start(self, event):
        if not self.started:
            if not event.keycode in [16, 17, 18]:
                self.started = True
                t = threading.Thread(target=self.time_thread)
                t.start()
        if not self.text_label.cget("text").startswith(self.text_entry.get()):
            self.text_entry.config(fg="orange")
        else:
            self.text_entry.config(fg="white")
        if self.text_entry.get() == self.text_label.cget("text")[:-1]:
            self.started = False
            self.text_entry.config(fg="blue")
    def time_thread(self):
        while self.started:
            time.sleep(0.1)
            self.counter += 0.1
            words_per_second = len(self.text_entry.get().split(" ")) / self.counter
            words_per_minute = words_per_second * 60
            self.type_label.config(text=f"Speed: \n{words_per_second:.2f} WordsPerSecond\n{words_per_minute:.2f} WordsPerMinute")

    def restart(self):
        self.started = False
        self.counter = 0
        self.type_label.config(text="Speed: \n0.00 WordsPerSecond\n0.00 WordsPerMinute")
        self.text_label.config(text=random.choice(self.texts))
        self.text_entry.delete(0, tk.END)

SpeedType()