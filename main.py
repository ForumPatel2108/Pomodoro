from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
# WORK_MIN = 25
# SHORT_BREAK_MIN = 5
# LONG_BREAK_MIN = 20
WORK_MIN = 1
SHORT_BREAK_MIN = 0.5
LONG_BREAK_MIN = 0.5
rep = 0
timer = None



# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canva.itemconfig(timer_txt,text="00:00")
    Tick_label.config(text="")
    global rep
    rep = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global rep
    rep += 1
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
 
    if (rep %8 == 0):
        count_down(long_break)
        label_timer.config(text="Long Break",fg=RED)
    elif(rep%2 == 0):
        count_down(short_break)
        label_timer.config(text="Break",fg=PINK)
    else:
        count_down(work_sec)
        label_timer.config(label_timer,text="Work",fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global timer

    count_min = math.floor(count/60)
    count_sec = count%60
    if count_sec < 10:
            count_sec = f"0{count_sec}"


    canva.itemconfig(timer_txt,text=f"{count_min}:{count_sec}")
    if(count > 0):
        timer = window.after(1000,count_down, count-1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(rep/2)
        for i in range(work_session):
            marks+="✔"
            Tick_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

label_timer = Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME, 35,"bold"))
label_timer.grid(row=0,column=1)

canva = Canvas(width=200,height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canva.create_image(100,112,image=tomato_img)
timer_txt = canva.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME, 35,"bold"))
canva.grid(row=1,column=1)
# count_down(5)

start_button = Button(text="Start",highlightthickness=0, command=start_timer)
start_button.grid(row=2,column=0)

reset_button = Button(text="Reset",highlightthickness=0,command=reset_timer)
reset_button.grid(row=2,column=2)

Tick_label = Label(text="",fg=GREEN,bg=YELLOW)
Tick_label.grid(row=3,column=1)

window.mainloop()