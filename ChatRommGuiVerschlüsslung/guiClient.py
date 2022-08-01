import tkinter as tk

root = tk.Tk()
root.title("chat")
root.geometry("400x600")
root.resizable(width=False, height=False)

eingabefeldWert = tk.StringVar()


def senden():
    label = tk.Label(root, text=eingabefeldWert.get()).pack(side="right")
    eingabefeldWert.set("")

eingabefeld = tk.Entry(root, textvariable= eingabefeldWert).pack(anchor="s", side="left", expand=True, fill="x", padx=10, pady = 10, ipady = 5)
b1 = tk.Button(root, text ="--->", command=senden).pack(anchor="s", side="left" , padx=10, pady = 10, ipady = 5)


root.mainloop()