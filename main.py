from tkinter import *
from tkinter import messagebox
from random_words import RandomWords

timer = None
BACKGROUND_COLOR = '#884A39'


def start_timer():
    countdown = 59
    new_timer(countdown)


def new_timer(count):
    count_secs = count * 1
    minute = '00:'
    if count_secs < 10:
        minute = '00:0'
    timer_label.config(text=f'Timer: {minute}{count_secs}')
    if count > 0:
        global timer
        timer = window.after(1000, new_timer, count - 1)
    else:
        high_score = ((50 - len(random_words)) / 50) * 60
        again = messagebox.askyesno(title="You lose!",
                                    message=f"Your WPM Score is {high_score}\n\n\n"
                                            f"* WPM - Words Per Minute\n\n"
                                            f"Do you want to play again?")
        if again:
            print('Yes')
        else:
            window.after(10000)
            window.destroy()


def werewolf():
    text2 = text_entry.get().replace(" ", "")
    for item in random_words:
        if text2 == item:
            text.config(state='normal')
            text.delete(1.0, END)
            random_words.remove(item)
            for dog in random_words:
                text.insert(END, dog + '   ')

            if len(random_words) == 0:
                messagebox.showinfo(title='Success',
                                    message=f"You've completed the challenge before the timer ran out.")


def get_text(event):
    if event.char == ' ':
        add_button.invoke()
        text_entry.delete(0, 'end')


words = RandomWords()
window = Tk()
window.title("Speed Typing Test")
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)

timer_label = Label(text="Timer: 00:00", font=("Courier", 20, "bold"))
timer_label.config(pady=10, padx=0, bg=BACKGROUND_COLOR, fg='#F9E0BB')
timer_label.grid(column=0, row=0)

heading_label = Label(text="TYPING SPEED TEST", font=("Courier", 50, "bold"))
heading_label.config(pady=20, padx=0, bg=BACKGROUND_COLOR, fg='#F9E0BB')
heading_label.grid(column=0, row=1)

heading_label = Label(text="How fast are your fingers? Do the one-minute typing test to find out.",
                      font=("Serif", 10, "bold"))
heading_label.config(pady=10, padx=0, bg=BACKGROUND_COLOR, fg='#F9E0BB')
heading_label.grid(column=0, row=2)
heading_label = Label(text="Press the Space Bar after each word. At the end, you'll get your typing speed in "
                           "WPM. Good luck!", font=("Serif", 10, "bold"))
heading_label.config(pady=20, padx=0, bg=BACKGROUND_COLOR, fg='#F9E0BB')
heading_label.grid(column=0, row=3)

text = Text(height=10, width=40, font=("Montserrat", 20), wrap="word")
random_words = words.random_words
for word in random_words:
    text.insert(END, word + '   ')

text.config(state='disabled', pady=20, bg='#FFC26F', fg='#fff')
text.grid(column=0, row=4)

text_entry = Entry(width=29, font=("Montserrat", 20), justify='center')
text_entry.focus()
text_entry.grid(column=0, row=5)
add_button = Button(text="Add Text", font=("Montserrat", 10, "bold"), command=werewolf)
text_entry.bind("<KeyPress>", get_text)
window.wait_visibility()
ready = messagebox.askyesno(title="Welcome to the Speed Typing Test", message="Are you ready to start?")
if ready:
    window.after(2000)
    start_timer()

else:
    window.destroy()

window.mainloop()
