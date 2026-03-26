import tkinter as tk

root = tk.Tk()
root.title("Mobile Calculator")
root.geometry("320x450")
root.configure(bg="black")

# Display
entry = tk.Entry(root, font=("Arial", 24), bd=10, relief="flat",
                 bg="black", fg="white", justify="right")
entry.pack(fill="both", ipadx=8, pady=10)

# Functions
def click(num):
    entry.insert(tk.END, num)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Button style
btn_style = {"font": ("Arial", 14), "bd": 0, "width": 5, "height": 2}

# Buttons frame
frame = tk.Frame(root, bg="black")
frame.pack()

buttons = [
    ('C', '%', '/',),
    ('7', '8', '9', '*'),
    ('4', '5', '6', '-'),
    ('1', '2', '3', '+'),
    ('0', '.', '=')
]

# Create buttons
for row in buttons:
    row_frame = tk.Frame(frame, bg="black")
    row_frame.pack(expand=True, fill="both")
    
    for btn in row:
        if btn == "C":
            action = clear
            color = "#700de2"
        elif btn == "=":
            action = calculate
            color = "#4CAF50"
        else:
            action = lambda x=btn: click(x)
            color = "#333333"
        
        tk.Button(row_frame, text=btn, bg=color, fg="white",
                  **btn_style, command=action).pack(side="left", expand=True, fill="both", padx=5, pady=5)

root.mainloop()