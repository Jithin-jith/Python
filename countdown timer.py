import time
from tkinter import messagebox, Tk

def countdown_timer(minutes, seconds):
    total_seconds = minutes * 60 + seconds
    while total_seconds:
        mins, secs = divmod(total_seconds, 60)
        timer = f'{mins:02d}:{secs:02d}'
        print(timer, end='\r')
        time.sleep(1)
        total_seconds -= 1

    # Show popup when timer ends
    root = Tk()
    root.withdraw()  # Hide the main window
    messagebox.showinfo("Time's Up!", "Your countdown has finished!")

# Get user input
try:
    mins = int(input("Enter minutes: "))
    secs = int(input("Enter seconds: "))
    countdown_timer(mins, secs)
except ValueError:
    print("Please enter valid integers!")