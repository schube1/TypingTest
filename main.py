import tkinter as tk
from tkinter import ttk, messagebox
import random
import time

sentences = {"The golden retriever jumped into the icy mountain lake.",
             "After dinner, they played cards under flickering lanterns.",
             "She hid the letter behind a loose brick in the fireplace.",
             "The spaceship vanished behind Saturn's glowing icy rings.",
             "He scribbled a note and taped it to the old mailbox door."
             }
root = tk.Tk()
root.title("Label Example")
root.geometry("450x200")

label_text = tk.StringVar()
label_text.set("Ready To Type?")
time_left = tk.StringVar()
time_left.set("Time Left: 60s")T

start_time = None
time_started = False
timer_running = False

entry = ttk.Entry(root)


label = ttk.Label(root, textvariable=label_text, font=("Arial", 16))
label.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")


time_label = ttk.Label(root, textvariable=time_left, font=("Arial", 12))
time_label.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")

def update_label():
    sentence = random.choice(list(sentences))
    label_text.set(sentence)
    entry.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
    update_button.grid_remove()


def check_complete(event): # check if we have the sentence fully written. triggered by every button release
    curr_text = entry.get()
    if curr_text == label_text.get():
        finish_test()       # if does match triggers finish_test()

entry.bind("<KeyRelease>", check_complete)

def finish_test(): # once we are done/have won we need to disable the entry box (cuz its cleaner) and use a message box to show the time it took to complete
    global timer_running
    timer_running = False
    elapsed = int(time.time() - start_time)
    label_text.set("You won!")
    entry.config(state="disabled")
    messagebox.showinfo(f"Finish Test", f"Completed in {elapsed} seconds")


def update_timer(): # triggered by the start of the timer, we need to continue loop thru until remaining is 0s then use message box to show loser stats. this shoudl be called every single second updating our tiem
    global start_time, timer_running
    if not timer_running:
        return
    elapsed = int( time.time() - start_time)
    remaining = max(0, 60-elapsed)
    time_left.set(f"Time Left: {remaining}s")
    if remaining > 0:
        root.after(1000, update_timer)
    else:
        entry.config(state='disabled')
        label_text.set("You lost!")
        messagebox.showinfo(f"Finish Test", "You lost!")
        timer_running = False


def start_timer(event): # we need to start a timer triggered by the first key press binded to the entry box, then only if the time isnt running already start it and call update_timer so we can have a live clock
    global start_time, time_started, timer_running
    if time_started == False:
        start_time = time.time()
        time_started = True
        timer_running = True
        update_timer()

entry.bind("<KeyPress>", start_timer)

update_button = ttk.Button(root, text="Start Game", command=update_label)
update_button.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

root.mainloop()


