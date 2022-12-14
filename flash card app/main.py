from tkinter import *
import pandas
import random

vocab = pandas.read_csv("vocab.csv")
words = vocab[vocab["status"] == 0]["word"]
new_words = words.to_list()
print(new_words)

translation_mode = 1
current_word = ""
score = 0

def randomise_words():
    word = random.choice(new_words)
    current_card.config(text=word)
    global current_word
    current_word = word

def remove_words(word):
    new_words.remove(word)

def show_translation():
    translation = vocab[vocab["word"] == current_word]["translation"]
    current_translation = translation.to_list()
    current_card.config(text=current_translation)

def show_current_word():
    flip_button.config(text="Show current word")
    current_card.config(text=current_word)

def flip_card():
    global translation_mode
    if translation_mode == 0:
        show_current_word()
        translation_mode = 1
    else:
        show_translation()
        translation_mode = 0

def mark_known_words():
    new_words.remove(current_word)
    randomise_words()
    global score
    score += 1
    score_display.config(text=f"{score}/400 Words Learned")


def next_card():
    randomise_words()



window = Tk()
window.config(width=600, height=500, padx=20, pady=20)

# Simple GUI

current_card = Label(text="Word")
current_card.grid(row=0, column=1)

no_button = Button(text="I don't know this word", command=next_card)
no_button.grid(row=1, column=0)

flip_button = Button(text="Show translation", command=flip_card)
flip_button.grid(row=1, column=1)

yes_button = Button(text="I know this word", command=mark_known_words)
yes_button.grid(row=1, column=2)

score_display = Label(text="0/400 Words Learned")
score_display.grid(row=2, column=1)

randomise_words()

window.mainloop()
