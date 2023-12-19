import tkinter as tk
from tkinter import ttk, messagebox
from ttkthemes import ThemedStyle  # Import modul theming

def sequential_search(data, target):
    for i, element in enumerate(data):
        if element == target:
            return i  # Mengembalikan indeks elemen yang ditemukan
    return -1  # Mengembalikan -1 jika elemen tidak ditemukan

def search_text_data():
    text_data = ["apel", "pisang", "ceri", "kurma", "mangga","semangka","pepaya"]
    target_text = entry.get()

    result_text = sequential_search(text_data, target_text)

    if result_text != -1:
        messagebox.showinfo("Hasil", f"Elemen '{target_text}' ditemukan pada indeks {result_text}.")
    else:
        messagebox.showinfo("Hasil", f"Elemen '{target_text}' tidak ditemukan.")

def search_numeric_data():
    numeric_data = [12, 34, 45, 56, 67, 89, 94]
    target_numeric = int(entry.get())

    result_numeric = sequential_search(numeric_data, target_numeric)

    if result_numeric != -1:
        messagebox.showinfo("Hasil", f"Elemen {target_numeric} ditemukan pada indeks {result_numeric}.")
    else:
        messagebox.showinfo("Hasil", f"Elemen {target_numeric} tidak ditemukan.")

root = tk.Tk()
root.title("Pencarian Data")

# Gaya yang lebih modern
style = ThemedStyle(root)
style.set_theme("arc")  # Tema yang digunakan (Anda dapat mencoba tema lain)

frame = ttk.Frame(root, padding="10")
frame.pack()

label_text = ttk.Label(frame, text="Masukkan teks yang ingin dicari:")
label_text.grid(row=0, column=0, sticky=tk.W, pady=(0, 10))

entry = ttk.Entry(frame)
entry.grid(row=0, column=1, padx=(0, 10))

button_search_text = ttk.Button(frame, text="Cari (Data Teks)", command=search_text_data)
button_search_text.grid(row=1, column=0, columnspan=2, pady=5)

button_search_numeric = ttk.Button(frame, text="Cari (Data Numerik)", command=search_numeric_data)
button_search_numeric.grid(row=2, column=0, columnspan=2, pady=5)

root.mainloop()
