import collections

text = "Hello  world!   How are you?"
space_count = collections.Counter(char for char in text if char.isspace())

print("Frekuensi karakter spasi:", space_count)
# Fungsi: Menggunakan Counter untuk menghitung jumlah karakter spasi.
# Kondisi: Ketika Anda ingin mendapatkan informasi mengenai karakter spasi dari teks.
