import collections

history = collections.deque(maxlen=5)  # Menyimpan maksimal 5 item dalam history

# Simulasi penambahan history
for i in range(10):
    history.append(f"Page {i+1}")

print("History terakhir (5 halaman):", list(history))
# Fungsi: Menggunakan deque untuk menyimpan sejarah terbatas.
# Kondisi: Ketika Anda ingin menyimpan batas riwayat dengan ukuran tertentu.
