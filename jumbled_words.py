import tkinter
from tkinter import *
import random
from tkinter import messagebox

answers = [
    "python",
    "java",
    "language",
    "english",
    "india",
    "company",
    "london",
    "computer",
    "mouse",
    "technology",
    "programming",
    "keyboard",
    "algorithm",
    "elephant",
    "sunshine",
    "butterfly",
    "mountain",
    "vacation",
    "ocean",
    "bicycle",
    "waterfall",
    "adventure",
    "celebrate",
    "wonderful",
    "chocolate",
    "rainbow",
    "treasure",
    "mystery",
    "blossom",
    "paradise"


]

words = [
    "nptoyh",
    "avja",
    "gualaneg",
    "shenigl",
    "aidin",
    "yanpomc",
    "odnlon",
    "ptercmou",
    "eousm",
    "chlogyteno",
    "garmmopnign",
    "drekoyab",
    "rigthomal",
    "tneepalh",
    "nnushise",
    "yturbeflt",
    "ntouamin",
    "aonvatic",
    "caeno",
    "ibcyecle",
    "fwtarefall",
    "ntueadver",
    "ltaebcere",
    "dfulewnor",
    "cothloatec",
    "wbionar",
    "artresue",
    "ysretmy",
    "msbolos",
    "aripsade"

]

num =  random.randrange(0, len(words), 1)

def default():
    global words,answers,num
    lbl.config(text = words[num])

def res():
    global words,answers,num
    num = random.randrange(0, len(words), 1)
    lbl.config(text = words[num])
    e1.delete(0, END)


def checkans():
    global words,answers,num
    var = e1.get()
    if var == answers[num]:
        messagebox.showinfo("Success", "This is a correct answer")
        res()
    else:
        messagebox.showerror("Error", "This is not Correct")
        e1.delete(0, END)

root = tkinter.Tk()
root.geometry("350x400+400+300")
root.title("Jumbled Word Game")
root.configure(background = "#000000")

lbl = Label(
    root,
    text = "Your here",
    font = ("Verdana", 18),
    bg = "#000000",
    fg = "#FFFFFF",
)
lbl.pack(pady = 30,ipady=10,ipadx=10)

ans1 = StringVar()
e1 = Entry(
    root,
    font = ("Verdana", 16),
    textvariable = ans1,
)
e1.pack(ipady=5,ipadx=5)

btncheck = Button(
    root,
    text = "Check",
    font = ("Comic sans ms", 16),
    width = 16,
    bg = "#4c4b4b",
    fg = "#6ab04c",
    relief = GROOVE,
    command = checkans,
)
btncheck.pack(pady = 40)

btnreset = Button(
    root,
    text = "Reset",
    font = ("Comic sans ms", 16),
    width = 16,
    bg = "#4c4b4b",
    fg = "#EA425C",
    relief = GROOVE,
    command = res,
)
btnreset.pack()

default()
root.mainloop()