import collections

def display_person_info(person):
    print(f"Name: {person.name}, Age: {person.age}")

Person = collections.namedtuple('Person', ['name', 'age'])
p1 = Person(name='Alice', age=25)

display_person_info(p1)
# Fungsi: Menggunakan data kelas untuk memudahkan penerusan data fungsi.
# Kondisi: Ketika Anda ingin mengelompokkan beberapa informasi terkait dalam fungsi.
