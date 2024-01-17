from tkinter import *
import pandas
from random import randint, choice
import time

FONT_NAME=('Arial', 20)
BACKGROUND_COLOR = "#B1DDC6"
to_learn={}
word={}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    print(original_data)
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def next_card():
    global word, flip_timer
    window.after_cancel(flip_timer)
    word = choice(to_learn)
    print(word)
    print(word['English'])
    canvas.itemconfig(change_title,text='French',fill='black')
    canvas.itemconfig(change_word, text=word['French'], fill='black')
    canvas.itemconfig(card_background, image=front_png)
    flip_timer=window.after(3000,flip_card)


def flip_card():
    # Adding English Card
    global word
    print(word)
    canvas.itemconfig(change_title, text='English',fill='white')
    canvas.itemconfig(change_word, text=word['English'],fill='white')
    canvas.itemconfig(card_background, image=back_png)

def is_known():
    to_learn.remove(word)
    print(len(to_learn))
    data=pandas.DataFrame(to_learn)
    data.to_csv('./data/words_to_learn.csv',index=False)
    next_card()

window = Tk()
window.title('Flashy')
window.config(padx=40,pady=20,bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# Adding Canvas image
canvas = Canvas(width=800,height=526)
front_png = PhotoImage(file='./images/card_front.png')
back_png = PhotoImage(file='./images/card_back.png')
card_background = canvas.create_image(400,270,image=front_png)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
change_title=canvas.create_text(400, 200, text='', font=('Arial', 15, 'italic'))
change_word=canvas.create_text(400, 270, text='', font=('Arial', 20,'bold'))
canvas.grid(column=0, row=0,columnspan=2)




#Button - Right
right_image=PhotoImage(file='./images/right.png')
right = Button(image=right_image,highlightthickness=0,command=is_known)
right.grid(column=0, row=1)

#Button - Left
left_image=PhotoImage(file='./images/wrong.png')
right = Button(image=left_image,highlightthickness=0,command=next_card)
right.grid(column=1, row=1)

next_card()

window.mainloop()

