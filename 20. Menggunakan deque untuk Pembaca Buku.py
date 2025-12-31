import collections

reading_list = collections.deque()

# Menambahkan judul buku
reading_list.append('Book 1')
reading_list.append('Book 2')
reading_list.append('Book 3')

# Mengambil buku yang sudah dibaca
finished_book = reading_list.popleft()

print("Buku yang sudah dibaca:", finished_book)
print("Buku yang tersisa untuk dibaca:", list(reading_list))
# Fungsi: Menjalankan proses membaca dengan deque.
# Kondisi: Ketika Anda ingin melacak buku yang dibaca dan yang akan dibaca.
