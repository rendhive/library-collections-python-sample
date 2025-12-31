import collections

Coordinate = collections.namedtuple('Coordinate', ['x', 'y'])

point1 = Coordinate(10, 20)
point2 = Coordinate(30, 40)

print("Koordinat Point 1:", point1)
print("Koordinat Point 2:", point2)
# Fungsi: Mewakili titik menggunakan namedtuples.
# Kondisi: Ketika Anda membutuhkan struktur data untuk menyimpan titik koordinat.
