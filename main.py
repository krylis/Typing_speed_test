from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random

words = ["fruit", "building", "alphabet", "kangaroo", "apple", "garage", "firefighter", "chicken", "skyscraper",
         "monster", "game", "fear", "computer", "window", "mattress", "hunger", "berserk", "sunset", "cloud",
         "earth", "angel", "devil", "junior", "africa", "continent", "humongous", "appetite", "vicious", "killer",
         "green", "miraculous", "powder", "valley", "numerous", "unanimous"]
words_typed = []
timer = 60


def get_random_word():
    num_of_words = len(words)
    random_index = random.randint(0, num_of_words-1)
    return words[random_index]


def countdown(second=0):
    word_entry['state'] = "normal"
    word_entry.focus_set()
    start_timer_btn['state'] = "disable"
    global timer
    timer = timer - second
    timer_text.set(get_timer_text())
    if timer > 0:
        root.after(1000, countdown, 1)
    else:
        restart_btn['state'] = "normal"
        word_entry.delete(0, END)
        word_entry['state'] = "disable"
        show_results()


def restart():
    global timer
    global words_typed
    timer = 60
    timer_text.set(get_timer_text())
    restart_btn['state'] = "disable"
    start_timer_btn['state'] = "normal"
    words_typed = []
    words_typed_text.set(get_words_typed_text())


def get_timer_text():
    return f"Timer: {timer} seconds"


def get_words_typed_text():
    return f"{len(words_typed)} Words Typed"


def compare_words(event):
    global words_typed
    if users_word.get() == random_word.get():
        words_typed.append(users_word.get())
        words_typed_text.set(get_words_typed_text())
    random_word.set(get_random_word())
    word_entry.delete(0, END)


def show_results():
    characters_typed = 0
    for word in words_typed:
        for c in word:
            characters_typed += 1
    typing_results = f"You typed {len(words_typed)} words in 60 seconds. \n" \
                     f"You averaged {characters_typed} characters typed per minute. \n" \
                     f"Great Work!"
    messagebox.showinfo(title="Results", message=typing_results)


root = Tk()
root.geometry("300x230")
root.title("Typing Speed Test")

random_word = StringVar()
random_word.set(get_random_word())
word_lbl = ttk.Label(root, textvariable=random_word, font=('Helvatical bold', 20))
word_lbl.pack(pady=5)

users_word = StringVar()
word_entry = ttk.Entry(root, textvariable=users_word, state="disable")
word_entry.pack(pady=5)

start_timer_btn = ttk.Button(root, text="Start Timer", command=countdown)
start_timer_btn.pack(pady=5)

instructions_label = ttk.Label(root, text="Hit Enter after each word")
instructions_label.pack(pady=5)

timer_text = StringVar()
timer_text.set(get_timer_text())
timer_label = ttk.Label(root, textvariable=timer_text)
timer_label.pack(pady=5)

words_typed_text = StringVar()
words_typed_text.set(get_words_typed_text())
words_typed_label = ttk.Label(root, textvariable=words_typed_text)
words_typed_label.pack(pady=5)

restart_btn = ttk.Button(root, text="Try Again", state="disable", command=restart)
restart_btn.pack()

root.bind('<Return>', compare_words)

root.mainloop()
