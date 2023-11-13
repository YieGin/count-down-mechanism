from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    miles_label.config(text="Timer")
    mark_label.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        miles_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        miles_label.config(text="Break", fg=RED)
        count_down(short_break_sec)
    else: 
        miles_label.config(text="Work")
        count_down(work_sec)
    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer =  window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✓"
        mark_label.config(text=mark)
        
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img =  PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img )
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# lABEL Timer
miles_label = Label(text="Timer")
miles_label.config(font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
miles_label.grid(column=1, row=0)

# lABEL ✓
mark_label = Label(text="")
mark_label.config(font=(FONT_NAME, 15, "bold"), bg=YELLOW, fg=GREEN)
mark_label.grid(column=1, row=5)

# Button Start
button = Button(text="Start", font=(FONT_NAME, 15, "bold"), highlightthickness=0, command=start_timer)
button.grid(column=0, row=4)

# Button Reset
button = Button(text="Reset", font=(FONT_NAME, 15, "bold"), highlightthickness=0, command=reset_timer)
button.grid(column=2, row=4)



window.mainloop()
