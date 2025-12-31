import collections

# Membuat namedtuple
Person = collections.namedtuple('Person', ['name', 'age'])
person = Person(name='John', age=30)

print("Nama:", person.name)
print("Usia:", person.age)
# Fungsi: Mendefinisikan objek data menggunakan namedtuple.
# Kondisi: Ketika Anda ingin mengelompokkan data terkait dengan cara yang terstruktur.
