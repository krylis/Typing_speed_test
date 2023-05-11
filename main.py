from tkinter import *
from tkinter import ttk
import random

words = ["fruit", "building", "alphabet", "kangaroo", "apple", "garage", "firefighter", "chicken", "skyscraper",
         "monster", "game", "fear", "computer", "window", "mattress", "hunger", "berserk", "sunset", "cloud",
         "earth", "angel", "devil", "junior", "africa", "continent", "humongous", "appetite", "vicious", "killer",
         "green", "miraculous", "powder", "valley", "numerous", "unanimous"]
timer = 60
words_typed = 0


def get_random_word():
    num_of_words = len(words)
    random_index = random.randint(0, num_of_words-1)
    return words[random_index]


def get_timer_text():
    return f"Timer: {timer} seconds"


def get_words_typed_text():
    return f"{words_typed} Words Typed"


root = Tk()
root.geometry("300x230")
root.title("Typing Speed Test")

random_word = StringVar()
random_word.set(get_random_word())
word_lbl = ttk.Label(root, textvariable=random_word, font=('Helvatical bold', 20))
word_lbl.pack(pady=5)

users_word = StringVar()
word_entry = ttk.Entry(root, textvariable=users_word)
word_entry.pack(pady=5)

instructions_label = ttk.Label(root, text="Start typing to begin \n Hit Enter after each word", justify="center")
instructions_label.pack(pady=5)

timer_text = StringVar()
timer_text.set(get_timer_text())
timer_label = ttk.Label(root, textvariable=timer_text)
timer_label.pack(pady=5)

words_typed_text = StringVar()
words_typed_text.set(get_words_typed_text())
words_typed_label = ttk.Label(root, textvariable=words_typed_text)
words_typed_label.pack(pady=5)

restart_btn = ttk.Button(root, text="Try Again", state="disable")
restart_btn.pack()

root.mainloop()