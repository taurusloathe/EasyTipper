import tkinter as tk
from tkinter import messagebox

def calculate_tip():
	subtotal = float(entry_subtotal.get())
	tip_percentage = float(entry_tip_percentage.get())

	tip_amount = (tip_percentage / 100) * subtotal
	total = subtotal + tip_amount

	label_tip_amount.config(text=f"Tip ({tip_percentage}%): ${tip_amount:.2f}", fg="#006400")  # green
	label_total.config(text=f"Total: ${total:.2f}", fg="#008000")  # teal

def clear_fields():
	entry_subtotal.delete(0, tk.END)
	entry_tip_percentage.delete(0, tk.END)
	label_tip_amount.config(text="Tip: $0.00", fg="#808080")  # gray
	label_total.config(text="Total: $0.00", fg="#808080")  # gray

root = tk.Tk()
root.title("Tip Calculator")
root.configure(background="#F0F0F0")  # light gray background

label_subtotal = tk.Label(root, text="Subtotal: $", bg="#F0F0F0", font=("Arial", 12, "bold"))  # light gray background
label_subtotal.pack(pady=10)
entry_subtotal = tk.Entry(root, bg="#FFFFFF", font=("Arial", 12))  # white background
entry_subtotal.pack(pady=10)

label_tip_percentage = tk.Label(root, text="Tip Percentage: ", bg="#F0F0F0", font=("Arial", 12, "bold"))  # light gray background
label_tip_percentage.pack(pady=10)
entry_tip_percentage = tk.Entry(root, bg="#FFFFFF", font=("Arial", 12))  # white background
entry_tip_percentage.pack(pady=10)

button_calculate = tk.Button(root, text="Calculate Tip", command=calculate_tip, bg="#0078D7", fg="#FFFFFF", font=("Arial", 12, "bold"), padx=10, pady=5)  # blue background and white text
button_calculate.pack(pady=10)

button_clear = tk.Button(root, text="Clear", command=clear_fields, bg="#0078D7", fg="#FFFFFF", font=("Arial", 12, "bold"), padx=10, pady=5)  # blue background and white text
button_clear.pack(pady=10)

label_tip_amount = tk.Label(root, text="Tip: $0.00", fg="#808080", bg="#F0F0F0", font=("Arial", 12))  # gray text and light gray background
label_tip_amount.pack(pady=10)
label_total = tk.Label(root, text="Total: $0.00", fg="#808080", bg="#F0F0F0", font=("Arial", 12))  # gray text and light gray background
label_total.pack(pady=10)

root.mainloop()
