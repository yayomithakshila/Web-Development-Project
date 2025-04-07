import tkinter as tk
from tkinter import messagebox

def submit():
    name = name_entry.get()
    email = email_entry.get()
    date = date_entry.get()
    time = time_entry.get()
    guests = guests_entry.get()
    
    if not (name and email and date and time and guests):
        messagebox.showerror("Error", "All fields are required!")
        return
    
    messagebox.showinfo("Success", f"Reservation confirmed for {name}\nDate: {date}\nTime: {time}\nGuests: {guests}")
    root.quit()

root = tk.Tk()
root.title("Reservation Form")

# Labels
tk.Label(root, text="Name:").grid(row=0, column=0)
tk.Label(root, text="Email:").grid(row=1, column=0)
tk.Label(root, text="Date (YYYY-MM-DD):").grid(row=2, column=0)
tk.Label(root, text="Time (HH:MM):").grid(row=3, column=0)
tk.Label(root, text="Number of Guests:").grid(row=4, column=0)

# Entry fields
name_entry = tk.Entry(root)
email_entry = tk.Entry(root)
date_entry = tk.Entry(root)
time_entry = tk.Entry(root)
guests_entry = tk.Entry(root)

name_entry.grid(row=0, column=1)
email_entry.grid(row=1, column=1)
date_entry.grid(row=2, column=1)
time_entry.grid(row=3, column=1)
guests_entry.grid(row=4, column=1)

# Submit button
tk.Button(root, text="Submit", command=submit).grid(row=5, column=0, columnspan=2)

root.mainloop()

# Labels
tk.Label(root, text="Contact:").grid(row=0, column=0)
tk.Label(root, text="Other:").grid(row=1, column=0)
tk.Label(root, text="Date (YYYY-MM-DD):").grid(row=2, column=0)
tk.Label(root, text="Time (HH:MM):").grid(row=3, column=0)
tk.Label(root, text="Number of users:").grid(row=4, column=0)

# Other information 
##changes done accordingly
tk.Label(root, text="Info:").grid(row=0, column=0)
tk.Label(root, text="Other:").grid(row=1, column=0)
tk.Label(root, text="Date (YYYY-MM-DD):").grid(row=2, column=0)
tk.Label(root, text="Time (HH:MM):").grid(row=3, column=0)
tk.Label(root, text="Other rooms:").grid(row=4, column=0)