import collections

values = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
counter = collections.Counter(values)

# Mengurutkan berdasarkan frekuensi
most_common = counter.most_common()

print("Item yang paling umum:", most_common)
# Fungsi: Mengambil item yang paling sering muncul dan urutkan berdasarkan frekuensi.
# Kondisi: Ketika Anda ingin mengidentifikasi elemen yang paling sering muncul.
