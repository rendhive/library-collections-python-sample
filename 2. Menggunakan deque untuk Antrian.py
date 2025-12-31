import collections

# Membuat deque
queue = collections.deque()

# Menambahkan item ke deque
queue.append('a')
queue.append('b')
queue.append('c')

print("Deque setelah penambahan:", queue)
# Fungsi: Menggunakan deque untuk penambahan dan pengurangan item dari kedua ujung.
# Kondisi: Ketika Anda memerlukan antrian dengan waktu akses cepat.
