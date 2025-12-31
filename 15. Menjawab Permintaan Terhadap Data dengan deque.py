import collections

requests = collections.deque()

# Menambahkan permintaan
requests.append('Request 1')
requests.append('Request 2')

# Mengelola permintaan
current_request = requests.popleft()

print("Memproses:", current_request)
print("Permintaan yang tersisa:", requests)
# Fungsi: Mengelola permintaan dalam antrian menggunakan deque.
# Kondisi: Ketika Anda ingin mengelola serangkaian tugas yang berurutan.
