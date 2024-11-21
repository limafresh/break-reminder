"""
Author: limafresh <https://github.com/limafresh>
License: CC0 <https://creativecommons.org/publicdomain/zero/1.0/>
"""

from tkinter import Tk, Label, Button, messagebox

root = Tk()
root.title("Break reminder")
root.resizable(0, 0)

remaining_time = 1200  # 20 minutes in seconds
is_timer_running = False
number_of_twenty = 0


def update_timer():
    global is_timer_running, remaining_time, number_of_twenty
    if is_timer_running:
        if remaining_time > 0:
            remaining_time -= 1
            # Division with remainder, 1st value, mins - quotient,
            # 2nd, secs - remainder
            mins, secs = divmod(remaining_time, 60)
            # 02 - displayed in 2 digits
            time_label["text"] = f"{mins:02}:{secs:02}"
            root.after(1000, update_timer)
        else:
            is_timer_running = False
            remaining_time = 1200
            time_label["text"] = "20:00"
            start_btn["state"] = "normal"
            pause_btn["state"] = "disabled"
            number_of_twenty += 1
            number_of_twenty_label["text"] = f"Number of 20-minutes: {number_of_twenty}"
            messagebox.showinfo(
                "Break!", "Look at objects 6 meters away for 20 seconds!"
            )


def start():
    global is_timer_running, remaining_time
    if not is_timer_running:
        is_timer_running = True
        start_btn["state"] = "disabled"
        pause_btn["state"] = "normal"
        update_timer()


def pause():
    global is_timer_running
    if is_timer_running:
        is_timer_running = False
        pause_btn["text"] = "Continue"
    else:
        is_timer_running = True
        pause_btn["text"] = "Pause"
        update_timer()


instruction = Label(text='When you sit down at the screen,\npress "Start"')
instruction.pack()

start_btn = Button(text="Start", command=start)
start_btn.pack()

pause_btn = Button(text="Pause", command=pause)
pause_btn.pack()
pause_btn["state"] = "disabled"

time_label = Label(text="20:00")
time_label.pack()

number_of_twenty_label = Label(text="Number of 20-minutes: 0")
number_of_twenty_label.pack()

root.mainloop()
