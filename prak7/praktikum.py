import tkinter as tk
from tkinter import messagebox

# Fungsi untuk memvalidasi input dan menampilkan hasil prediksi
def hasil_prediksi():
    try:
        for entry in labels_input:
            nilai = int(entry.get())  # Mengambil nilai dari setiap input dan mengonversinya ke integer
            if not (0 <= nilai <= 100):  # Memeriksa apakah nilai berada antara 0 dan 100
                raise ValueError("Nilai harus antara 0 dan 100.")  # Jika tidak, raise ValueError
        hasil_label.config(text="Prediksi Prodi: Teknologi Informasi")  # Menampilkan prediksi jika semua input valid
    except ValueError:
        messagebox.showerror("Input Error", "Pastikan semua input adalah angka antara 0 dan 100.")  # Pesan error jika ada input invalid

# Inisialisasi jendela utama aplikasi
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")  # Judul jendela aplikasi
root.geometry("400x600")  # Ukuran jendela aplikasi
root.configure(bg="#f0f0f0")  # Warna latar belakang aplikasi

# Membuat label judul untuk aplikasi
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 14, "bold"))
judul_label.grid(row=0, column=0, columnspan=2, pady=10)  # Menempatkan label judul di bagian atas

# Membuat list untuk menyimpan input nilai mata pelajaran
labels_input = []
for i in range(10):
    # Membuat label untuk setiap mata pelajaran
    mata_pelajaran_label = tk.Label(root, text=f"Nilai Mata Pelajaran {i+1}:")
    mata_pelajaran_label.grid(row=i+1, column=0, sticky="e", padx=10, pady=5)  # Menempatkan label di grid
    # Membuat kolom input untuk nilai mata pelajaran
    input_value = tk.Entry(root)
    input_value.grid(row=i+1, column=1, padx=10, pady=5)  # Menempatkan kolom input di grid
    labels_input.append(input_value)  # Menyimpan kolom input di list labels_input

# Membuat tombol untuk memicu prediksi
prediksi_button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi)
prediksi_button.grid(row=11, column=0, columnspan=2, pady=20)  # Menempatkan tombol di bawah input nilai

# Membuat label untuk menampilkan hasil prediksi
hasil_label = tk.Label(root, text="", font=("Arial", 12))
hasil_label.grid(row=12, column=0, columnspan=2, pady=10)  # Menempatkan label hasil di bawah tombol

# Menjalankan aplikasi
root.mainloop()
