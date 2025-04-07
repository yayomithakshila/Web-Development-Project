Create API 

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
tk.Button(root, text="Submit", command=submit).grid(row=5, column=0, columnspan=2