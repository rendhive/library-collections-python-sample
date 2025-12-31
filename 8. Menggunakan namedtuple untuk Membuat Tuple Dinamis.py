import collections

# Membuat namedtuple
Point = collections.namedtuple('Point', ['x', 'y'])
p = Point(10, 20)

print("Point:", p)
print("x:", p.x, "y:", p.y)
# Fungsi: Membuat tuple dengan nama untuk setiap elemen.
# Kondisi: Ketika Anda ingin menggunakan tuple dengan pengenalan atribut untuk mengakses elemen.
