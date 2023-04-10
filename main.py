import tkinter as tk

def dec_to_all():
    # Mendapatkan nilai dari inputan desimal
    dec_value = dec_entry.get()
    # Memeriksa apakah nilai tersebut merupakan angka (integer)
    if dec_value.isdigit(): 
        # Mengkonversi nilai desimal menjadi biner, oktal, heksadesimal, dan ASCII
        dec_value = int(dec_value)
        bin_value = bin(dec_value)[2:]
        oct_value = oct(dec_value)[2:]
        hex_value = hex(dec_value)[2:].upper()
        ascii_value = chr(dec_value)
        # Menghapus nilai lama pada inputan biner, oktal, heksadesimal, dan ASCII
        bin_entry.delete(0, tk.END)
        oct_entry.delete(0, tk.END)
        hex_entry.delete(0, tk.END)
        ascii_entry.delete(0, tk.END)
        # Memasukkan nilai yang telah dikonversi ke dalam inputan biner, oktal, heksadesimal, dan ASCII
        bin_entry.insert(0, bin_value)
        oct_entry.insert(0, oct_value)
        hex_entry.insert(0, hex_value)
        ascii_entry.insert(0, ascii_value)
    else:
        # Menampilkan pesan error jika input bukan merupakan angka (integer)
        tk.messagebox.showerror("Error", "Input is not a valid integer")

def bin_to_all():
    # Mendapatkan nilai dari inputan biner
    bin_value = bin_entry.get()
    # Memeriksa apakah nilai tersebut merupakan angka biner
    if bin_value.isdigit():
        # Mengkonversi nilai biner menjadi desimal, oktal, heksadesimal, dan ASCII
        dec_value = int(bin_value, 2)
        oct_value = oct(dec_value)[2:]
        hex_value = hex(dec_value)[2:].upper()
        ascii_value = chr(dec_value)
        # Menghapus nilai lama pada inputan desimal, oktal, heksadesimal, dan ASCII
        dec_entry.delete(0, tk.END)
        oct_entry.delete(0, tk.END)
        hex_entry.delete(0, tk.END)
        ascii_entry.delete(0, tk.END)
        # Memasukkan nilai yang telah dikonversi ke dalam inputan desimal, oktal, heksadesimal, dan ASCII
        dec_entry.insert(0, dec_value)
        oct_entry.insert(0, oct_value)
        hex_entry.insert(0, hex_value)
        ascii_entry.insert(0, ascii_value)
    else:
        # Menampilkan pesan error jika input bukan merupakan angka biner
        tk.messagebox.showerror("Error", "Input is not a valid binary number")

def oct_to_all():
    # Mendapatkan nilai dari inputan oktal
    oct_value = oct_entry.get()
    # Memeriksa apakah nilai tersebut merupakan angka oktal
    if oct_value.isdigit():
        # Mengkonversi nilai oktal menjadi desimal, biner, heksadesimal, dan ASCII
        dec_value = int(oct_value, 8)
        bin_value = bin(dec_value)[2:]
        hex_value = hex(dec_value)[2:].upper()
        ascii_value = chr(dec_value)
        # Menghapus nilai lama pada inputan desimal, biner, heksadesimal, dan ASCII
        dec_entry.delete(0, tk.END)
        bin_entry.delete(0, tk.END)
        hex_entry.delete(0, tk.END)
        ascii_entry.delete(0, tk.END)
        # Memasukkan nilai yang telah dikonversi ke dalam inputan desimal, biner, heksadesimal, dan ASCII
        dec_entry.insert(0, dec_value)
        bin_entry.insert(0, bin_value)
        hex_entry.insert(0, hex_value)
        ascii_entry.insert(0, ascii_value)
    else:
        # Menampilkan pesan error jika input bukan merupakan angka oktal
        tk.messagebox.showerror("Error", "Input is not a valid octal number")

def hex_to_all():
    # Mendapatkan nilai dari inputan heksadesimal dan mengubahnya menjadi huruf kapital
    hex_value = hex_entry.get().upper()
        # Mengkonversi nilai heksadesimal menjadi desimal, biner, oktal, dan ASCII
    dec_value = int(hex_value, 16)
    bin_value = bin(dec_value)[2:]
    oct_value = oct(dec_value)[2:]
    ascii_value = chr(dec_value)
    # Menghapus nilai lama pada inputan desimal, biner, oktal, dan ASCII
    dec_entry.delete(0, tk.END)
    bin_entry.delete(0, tk.END)
    oct_entry.delete(0, tk.END)
    ascii_entry.delete(0, tk.END)
    # Memasukkan nilai yang telah dikonversi ke dalam inputan desimal, biner, oktal, dan ASCII
    dec_entry.insert(0, dec_value)
    bin_entry.insert(0, bin_value)
    oct_entry.insert(0, oct_value)
    ascii_entry.insert(0, ascii_value)

def str_to_ascii():
    # Mendapatkan nilai dari inputan string
    string_value = str_entry.get()
    # Menyimpan nilai ASCII dalam bentuk string
    ascii_value = ""
    # Melakukan iterasi pada setiap karakter dalam string
    for char in string_value:
        # Mengambil nilai ASCII dari karakter saat ini menggunakan fungsi Python ord() (menghasilkan sebuah nilai integer berupa kode ASCII dari sebuah karakter)
        ascii_value += str(ord(char)) + " "
    # Menghapus nilai lama pada inputan ASCII
    ascii_entry.delete(0, tk.END)
    # Memasukkan nilai ASCII yang telah dihasilkan ke dalam inputan ASCII
    ascii_entry.insert(0, ascii_value)
    
def delete_all():
    # Menghapus semua nilai pada inputan desimal
    dec_entry.delete(0, tk.END)
    # Menghapus semua nilai pada inputan biner
    bin_entry.delete(0, tk.END)
    # Menghapus semua nilai pada inputan oktal
    oct_entry.delete(0, tk.END)
    # Menghapus semua nilai pada inputan heksadesimal
    hex_entry.delete(0, tk.END)
    # Menghapus semua nilai pada inputan ASCII
    ascii_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Konversi Bilangan")
root.geometry("680x300")
root.configure(bg="#E8E8E8")

dec_label = tk.Label(root, text="Desimal:", font=("Helvetica", 14), bg="#E8E8E8", fg="black")
dec_label.grid(row=0, column=0, padx=5, pady=5)
dec_entry = tk.Entry(root, font=("Helvetica", 14))
dec_entry.grid(row=0, column=1, padx=5, pady=5)

bin_label = tk.Label(root, text="Biner:", font=("Helvetica", 14), bg="#E8E8E8", fg="black")
bin_label.grid(row=1, column=0, padx=5, pady=5)
bin_entry = tk.Entry(root, font=("Helvetica", 14))
bin_entry.grid(row=1, column=1, padx=5, pady=5)

oct_label = tk.Label(root, text="Oktal:", font=("Helvetica", 14), bg="#E8E8E8", fg="black")
oct_label.grid(row=2, column=0, padx=5, pady=5)
oct_entry = tk.Entry(root, font=("Helvetica", 14))
oct_entry.grid(row=2, column=1, padx=5, pady=5)

hex_label = tk.Label(root, text="Hexadesimal:", font=("Helvetica", 14), bg="#E8E8E8", fg="black")
hex_label.grid(row=3, column=0, padx=5, pady=5)
hex_entry = tk.Entry(root, font=("Helvetica", 14))
hex_entry.grid(row=3, column=1, padx=5, pady=5)

str_label = tk.Label(root, text="String:", font=("Helvetica", 14), bg="#E8E8E8", fg="black")
str_label.grid(row=4, column=0, padx=5, pady=5)
str_entry = tk.Entry(root, font=("Helvetica", 14))
str_entry.grid(row=4, column=1, padx=5, pady=5)

ascii_label = tk.Label(root, text="ASCII:", font=("Helvetica", 14), bg="#E8E8E8", fg="black")
ascii_label.grid(row=5, column=0, padx=5, pady=5)
ascii_entry = tk.Entry(root, font=("Helvetica", 14))
ascii_entry.grid(row=5, column=1, padx=5, pady=5)

dec_to_all_button = tk.Button(root, text="Konversi", command=dec_to_all, bg="#4681f4", fg="white", font=("Helvetica", 14))
dec_to_all_button.grid(row=0, column=2, padx=5, pady=5)

bin_to_all_button = tk.Button(root, text="Konversi", command=bin_to_all, bg="#4681f4", fg="white", font=("Helvetica", 14))
bin_to_all_button.grid(row=1, column=2, padx=5, pady=5)

oct_to_all_button = tk.Button(root, text="Konversi", command=oct_to_all, bg="#4681f4", fg="white", font=("Helvetica", 14))
oct_to_all_button.grid(row=2, column=2, padx=5, pady=5)

hex_to_all_button = tk.Button(root, text="Konversi", command=hex_to_all, bg="#4681f4", fg="white", font=("Helvetica", 14))
hex_to_all_button.grid(row=3, column=2, padx=5, pady=5)

str_to_ascii_button = tk.Button(root, text="Konversi ke ASCII", command=str_to_ascii, bg="#4681f4", fg="white", font=("Helvetica", 14))
str_to_ascii_button.grid(row=4, column=2, padx=5, pady=5)

delete_all_button = tk.Button(root, text="Delete All", command=delete_all, bg="#FF0000", fg="white", font=("Helvetica", 14))
delete_all_button.grid(row=0, column=3, padx=5, pady=5)

root.mainloop()