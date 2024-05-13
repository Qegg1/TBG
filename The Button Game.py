import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def Destroy():
    global root
    root.destroy()

def Incorrect():
    color = color_variable.get()
    incorrect_window = tk.Toplevel()
    incorrect_window.geometry("80x55")
    incorrect_window.title("The Button Game")
    incorrect_window.config(background = color)
    ttk.Label(incorrect_window, text = "That's Incorrect!").pack()
    ttk.Button(incorrect_window, text = "OK", width = 15, command = Destroy).pack()
    
def Continue():
    second_window = tk.Toplevel()
    second_window.config(background = "gray")
    second_window.geometry("300x135")
    second_window.title("The Button Game")
    ttk.Label(second_window, text = "Are you sure that you wish to continue?").pack()
    ttk.Button(second_window, text = "Yes", width = 15, command = Yes).pack()
    ttk.Button(second_window, text = "No", width = 15, command = No).pack()

def Yes():
    name = name_entry.get()
    third_window = tk.Toplevel()
    third_window.config(background = "gray")
    third_window.geometry("325x135")
    third_window.title("The Button Game")
    ttk.Label(third_window, text = "I'm sorry, " + str(name) + ", but you're too eager to play this game.").pack()
    ttk.Button(third_window, text = "OK", width = 15, command = Destroy).pack()

def No():
    fourth_window = tk.Toplevel()
    fourth_window.config(background = "gray")
    fourth_window.geometry("325x135")
    fourth_window.title("The Button Game")
    ttk.Label(fourth_window, text = "Why are you so hesitant? This is going to be fun! >:)").pack()
    ttk.Button(fourth_window, text = "Uh Oh", width = 15, command = Age).pack()

def Age():
    name = name_entry.get()
    fifth_window = tk.Toplevel()
    fifth_window.config(background = "gray")
    fifth_window.geometry("325x135")
    fifth_window.title("The Button Game")
    ttk.Label(fifth_window, text = "Let's start with something easy, " + str(name) + ". What is your age?").pack()
    age_entry = ttk.Entry(fifth_window, textvariable = age_variable, font = "Arial 13").pack()
    ttk.Button(fifth_window, text = "Next", width = 15, command = Question2).pack()

def Question2():
    age = age_variable.get()
    question2_window = tk.Toplevel()
    question2_window.config(background = "gray")
    question2_window.geometry("385x135")
    question2_window.title("The Button Game")
    ttk.Label(question2_window, text = "Wow, you're " + str(age) + "? You look much older to me.").pack()
    ttk.Label(question2_window, text = "Anyway, I want to get to know you better. What is your favorite color?").pack()
    color_entry = ttk.Entry(question2_window, textvariable = color_variable, font = "Arial 13").pack()
    ttk.Button(question2_window, text = "Showtime!", width = 15, command = Question3).pack()

def Question3():
    color = color_variable.get()
    question3_window = tk.Toplevel()
    question3_window.geometry("420x180")
    question3_window.title("The Button Game")
    question3_window.config(background = color)
    ttk.Label(question3_window, text = "That's a nice change of pace.").pack()
    ttk.Label(question3_window, text = "Let's finish up with a series of math questions. I want to test your knowledge!").pack()
    ttk.Label(question3_window, text = "What is 2 + 2?").pack()
    ttk.Button(question3_window, text = "0", width = 15, command = Incorrect).pack()
    ttk.Button(question3_window, text = "2", width = 15, command = Incorrect).pack()
    ttk.Button(question3_window, text = "4", width = 15, command = Question4).pack()
    ttk.Button(question3_window, text = "22", width = 15, command = Incorrect).pack()

def Question4():
    color = color_variable.get()
    question4_window = tk.Toplevel()
    question4_window.geometry("325x180")
    question4_window.title("The Button Game")
    question4_window.config(background = color)
    ttk.Label(question4_window, text = "That was too easy. Let's make things more difficult.").pack()
    ttk.Label(question4_window, text = "What is 121 - 88?").pack()
    ttk.Button(question4_window, text = "28", width = 15, command = Incorrect).pack()
    ttk.Button(question4_window, text = "33", width = 15, command = Question5).pack()
    ttk.Button(question4_window, text = "35", width = 15, command = Incorrect).pack()
    ttk.Button(question4_window, text = "53", width = 15, command = Incorrect).pack()

def Question5():
    color = color_variable.get()
    name = name_entry.get()
    question4_window = tk.Toplevel()
    question4_window.geometry("325x180")
    question4_window.title("The Button Game")
    question4_window.config(background = color)
    ttk.Label(question4_window, text = "You're pretty good, " + str(name) + ". Time to get serious.").pack()
    ttk.Label(question4_window, text = "What is 555/3?").pack()
    ttk.Button(question4_window, text = "180", width = 15, command = Incorrect).pack()
    ttk.Button(question4_window, text = "183", width = 15, command = Incorrect).pack()
    ttk.Button(question4_window, text = "185", width = 15, command = Final).pack()
    ttk.Button(question4_window, text = "188", width = 15, command = Incorrect).pack()

def Final():
    age = age_variable.get()
    color = color_variable.get()
    question4_window = tk.Toplevel()
    question4_window.geometry("405x180")
    question4_window.title("The Button Game")
    question4_window.config(background = color)
    ttk.Label(question4_window, text = "Wow! I'm very impressed. This is the final question. Good luck >:)").pack()
    ttk.Label(question4_window, text = "What is 100 + your age * 3 - 25?").pack()
    textvariable1 = 100 + (int(age) * 3) - 25
    textvariable2 = 100 + (int(age) * 3) - 15
    textvariable3 = 100 + (int(age) * 3) - 35
    textvariable4 = 105 + (int(age) * 3) - 25
    ttk.Button(question4_window, text = textvariable1, width = 15, command = Congratulations).pack()
    ttk.Button(question4_window, text = textvariable2, width = 15, command = Incorrect).pack()
    ttk.Button(question4_window, text = textvariable3, width = 15, command = Incorrect).pack()
    ttk.Button(question4_window, text = textvariable4, width = 15, command = Incorrect).pack()

def Congratulations():
    color = color_variable.get()
    congratulations_window = tk.Toplevel()
    congratulations_window.geometry("300x135")
    congratulations_window.title("The Button Game")
    congratulations_window.config(background = color)
    ttk.Label(congratulations_window, text = "Congratulations! You have completed The Button Game!").pack()
    ttk.Button(congratulations_window, text = "Goodbye!", width = 15, command = Destroy).pack()
            
root = tk.Tk()
root.config(background = "gray")
root.geometry("300x135")
root.title("The Button Game")

age_variable = tk.StringVar()
color_variable = tk.StringVar()
name_label = tk.Label(root, text = "Welcome to The Button Game. What is your name?")
name_label.grid(row = 0, column = 0, padx = 13, pady = 15)
name_entry = tk.Entry(root, font = "Arial 13")
name_entry.grid(row = 1, column = 0)

continue_button = tk.Button(root, text = "Continue", font = "Arial 13", width = 15, command = Continue)
continue_button.grid(row = 5, column = 0, padx = 5, pady = 15)

root.mainloop()

"""
    if color == "Blue" or "blue":
        question3_window.config(background = "blue")
    elif color == "Black" or "black":
        question3_window.config(background = "black")
    elif color == "Pink" or "pink":
        question3_window.config(background = "pink")
    elif color == "White" or "white":
        question3_window.config(background = "white")
    elif color == "Green" or "green":
        question3_window.config(background = "green")
    elif color == "Red" or "red":
        question3_window.config(background = "red")
    elif color == "Yellow" or "yellow":
        question3_window.config(background = "yellow")
    elif color == "Orange" or "orange":
        question3_window.config(background = "orange")
    elif color == "Purple" or "purple":
        question3_window.config(background = "purple")
    elif color == "Gray" or "gray":
        question3_window.config(background = "gray")
        ttk.Label(question3_window, text = "That's my favorite color too! I like you. :)").pack()
    else:
        question3_window.config(background = "gray")
        ttk.Label(question3_window, text = "I'm not programmed to reconize that color.").pack()
"""


