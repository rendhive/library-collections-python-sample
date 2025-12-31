import collections

queue = collections.deque(['a', 'b', 'c'])

# Menghapus item dari depan
first_item = queue.popleft()

print("Item pertama yang diambil:", first_item)
print("Deque setelah penghapusan:", queue)
# Fungsi: Menghapus item dari depan deque.
# Kondisi: Ketika Anda perlu mengelola antrian dengan efisiensi tinggi.
