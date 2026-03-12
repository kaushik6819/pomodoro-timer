import tkinter
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25 
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps =0
timer =None


def reset_timer():
    #This resets the timer 
    window.after_cancel(timer)
    canvas.itemconfig(time,text=f"00:00")
    label["text"]="Timer"
    check["text"]=""
    global reps
    reps=0


def start_timer():
    #start the timer
    global reps
    reps +=1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 !=0:
        count_timer(work_sec)
        label["text"]="Timer"
        label["foreground"]=GREEN
    elif reps % 8==0:
        count_timer(long_break_sec)
        label["text"]="Break"
        label["foreground"]=RED

    else:
        count_timer(short_break_sec)
        label["text"]="Break"
        label["foreground"]=PINK
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_timer(count):
    #countdown function
    count_min = math.floor(count/60)
    count_sec= count % 60
    if count_sec<10:
        count_sec=f"0{count_sec}"

    #itemconfig is used to modefy the countdown text in screen
    canvas.itemconfig(time,text=f"{count_min}:{count_sec}")
    if count >0:
        global timer
        #window.after is used to count the time in min
        timer = window.after(1000,count_timer,count-1)
    else:
        start_timer()
        check["text"] = "✔" * (reps//2)


# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Promodromo Timer")
window.config(padx=50,pady=30,bg= YELLOW)

label = tkinter.Label(text="Timer",font=(FONT_NAME,35,"bold"),bg=YELLOW,foreground=GREEN)
label.grid(column=1,row=0)

tomato_img = tkinter.PhotoImage(file= "tomato.png")
canvas = tkinter.Canvas(width = 200, height=224,bg=YELLOW,highlightthickness=0)
canvas.create_image(100,112, image=tomato_img)
time = canvas.create_text(106,135,text="00:00",font=(FONT_NAME,30,"bold"),fill ="white")
canvas.grid(column=1,row=1)

start = tkinter.Button(text="Start",highlightthickness=0,command=start_timer)
start.grid(column=0,row=2)

reset=tkinter.Button(text="Reset",highlightthickness=0,command=reset_timer)
reset.grid(column=2,row=2)

check = tkinter.Label(text="",font=(FONT_NAME,14),bg=YELLOW,fg=GREEN)
check.grid(column=1,row=3)



window.mainloop()
