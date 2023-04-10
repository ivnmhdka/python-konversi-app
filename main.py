import tkinter as tk

def dec_to_all():
    dec_value = int(dec_entry.get())
    bin_value = bin(dec_value)[2:]
    oct_value = oct(dec_value)[2:]
    hex_value = hex(dec_value)[2:].upper()
    ascii_value = chr(dec_value)
    bin_entry.delete(0, tk.END)
    oct_entry.delete(0, tk.END)
    hex_entry.delete(0, tk.END)
    ascii_entry.delete(0, tk.END)
    bin_entry.insert(0, bin_value)
    oct_entry.insert(0, oct_value)
    hex_entry.insert(0, hex_value)
    ascii_entry.insert(0, ascii_value)

def bin_to_all():
    bin_value = bin_entry.get()
    dec_value = int(bin_value, 2)
    oct_value = oct(dec_value)[2:]
    hex_value = hex(dec_value)[2:].upper()
    ascii_value = chr(dec_value)
    dec_entry.delete(0, tk.END)
    oct_entry.delete(0, tk.END)
    hex_entry.delete(0, tk.END)
    ascii_entry.delete(0, tk.END)
    dec_entry.insert(0, dec_value)
    oct_entry.insert(0, oct_value)
    hex_entry.insert(0, hex_value)
    ascii_entry.insert(0, ascii_value)

def oct_to_all():
    oct_value = oct_entry.get()
    dec_value = int(oct_value, 8)
    bin_value = bin(dec_value)[2:]
    hex_value = hex(dec_value)[2:].upper()
    ascii_value = chr(dec_value)
    dec_entry.delete(0, tk.END)
    bin_entry.delete(0, tk.END)
    hex_entry.delete(0, tk.END)
    ascii_entry.delete(0, tk.END)
    dec_entry.insert(0, dec_value)
    bin_entry.insert(0, bin_value)
    hex_entry.insert(0, hex_value)
    ascii_entry.insert(0, ascii_value)

def hex_to_all():
    hex_value = hex_entry.get().upper()
    dec_value = int(hex_value, 16)
    bin_value = bin(dec_value)[2:]
    oct_value = oct(dec_value)[2:]
    ascii_value = chr(dec_value)
    dec_entry.delete(0, tk.END)
    bin_entry.delete(0, tk.END)
    oct_entry.delete(0, tk.END)
    ascii_entry.delete(0, tk.END)
    dec_entry.insert(0, dec_value)
    bin_entry.insert(0, bin_value)
    oct_entry.insert(0, oct_value)
    ascii_entry.insert(0, ascii_value)

def str_to_ascii():
    string_value = str_entry.get()
    ascii_value = ""
    for char in string_value:
        ascii_value += str(ord(char)) + " "
    ascii_entry.delete(0, tk.END)
    ascii_entry.insert(0, ascii_value)

root = tk.Tk()
root.title("Konversi Bilangan")
root.geometry("400x300")

dec_label = tk.Label(root, text="Desimal:")
dec_label.grid(row=0, column=0, padx=5, pady=5)
dec_entry = tk.Entry(root)
dec_entry.grid(row=0, column=1, padx=5, pady=5)

bin_label = tk.Label(root, text="Biner:")
bin_label.grid(row=1, column=0, padx=5, pady=5)
bin_entry = tk.Entry(root)
bin_entry.grid(row=1, column=1, padx=5, pady=5)

oct_label = tk.Label(root, text="Oktal:")
oct_label.grid(row=2, column=0, padx=5, pady=5)
oct_entry = tk.Entry(root)
oct_entry.grid(row=2, column=1, padx=5, pady=5)

hex_label = tk.Label(root, text="Hexadesimal:")
hex_label.grid(row=3, column=0, padx=5, pady=5)
hex_entry = tk.Entry(root)
hex_entry.grid(row=3, column=1, padx=5, pady=5)

str_label = tk.Label(root, text="String:")
str_label.grid(row=4, column=0, padx=5, pady=5)
str_entry = tk.Entry(root)
str_entry.grid(row=4, column=1, padx=5, pady=5)

ascii_label = tk.Label(root, text="ASCII:")
ascii_label.grid(row=5, column=0, padx=5, pady=5)
ascii_entry = tk.Entry(root)
ascii_entry.grid(row=5, column=1, padx=5, pady=5)

dec_to_all_button = tk.Button(root, text="Konversi", command=dec_to_all)
dec_to_all_button.grid(row=0, column=2, padx=5, pady=5)

bin_to_all_button = tk.Button(root, text="Konversi", command=bin_to_all)
bin_to_all_button.grid(row=1, column=2, padx=5, pady=5)

oct_to_all_button = tk.Button(root, text="Konversi", command=oct_to_all)
oct_to_all_button.grid(row=2, column=2, padx=5, pady=5)

hex_to_all_button = tk.Button(root, text="Konversi", command=hex_to_all)
hex_to_all_button.grid(row=3, column=2, padx=5, pady=5)

str_to_ascii_button = tk.Button(root, text="Konversi ke ASCII", command=str_to_ascii)
str_to_ascii_button.grid(row=4, column=2, padx=5, pady=5)

root.mainloop()