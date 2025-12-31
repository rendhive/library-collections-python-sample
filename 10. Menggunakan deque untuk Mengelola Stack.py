import collections

stack = collections.deque()

# Menambahkan item ke stack
stack.append('a')
stack.append('b')
stack.append('c')

# Menghapus item dari stack
top_item = stack.pop()

print("Item teratas dari stack:", top_item)
print("Stack setelah pop:", stack)
# Fungsi: Mengelola stack menggunakan deque.
# Kondisi: Ketika Anda memerlukan struktur data LIFO.
