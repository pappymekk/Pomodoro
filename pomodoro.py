# Studying during 25 minutes and getting a break of 5 minutes,
# and then approving either for restudying or finishing the work

import datetime
from tkinter import *
import tkinter.messagebox


def welcoming():
    """Welcoming the user, and asking him to click the button "OK" """
    root = Tk()
    root.withdraw()  # hide the root window
    tkinter.messagebox.showinfo("Pomodoro", "Welcome to Pomodoro! Click OK to activate it :)")


def take_break():
    """This function asks the user if he wants to take a break of 5 minutes"""
    dialog = Tk()
    dialog.withdraw()
    result = tkinter.messagebox.askquestion("Pomodoro", "Would you like to have a 5 minutes break?")
    if result == 'yes':  # If the button 'yes' is clicked
        return True
    else:  # If the button 'no' is clicked
        return False


def restudying():
    """The function asks the user if he wants to restudy after taking a break"""
    dialog = Tk()
    dialog.withdraw()
    result = tkinter.messagebox.askquestion("Pomodoro", "Would you like to re-work for 25 minutes?")
    if result == 'yes':  # If the button 'yes' is clicked
        return True
    else:  # If the button 'no' is clicked
        return False


def farewell():
    """This function shows a message to farewell the user"""
    root = Tk()
    root.withdraw()  # hide the root window
    tkinter.messagebox.showinfo("Pomodoro", "Your work is done! See you again :)")


print(welcoming())


def studying():
    start = datetime.datetime.now()  # The start time
    ending = start + datetime.timedelta(minutes=25)  # The expected time for the end
    while datetime.datetime.now() != ending:  # the current time is not 25 minutes past the start
        continue
    approval = take_break()
    if approval:  # If there's an approval for the break
        start_rest = datetime.datetime.now()  # The beginning of the nap time
        end_rest = start_rest + datetime.timedelta(minutes=5)
        while datetime.datetime.now() != end_rest:  # the current time is not 5 minutes past the start of the nap
            continue
        study_approval = restudying()
        if study_approval:  # If studying again is approved
            return studying()
        else:  # If studying again not approved
            return farewell()
    else:
        return studying()


print(studying())
