import collections

ordered_dict = collections.OrderedDict()
ordered_dict['item1'] = 100
ordered_dict['item2'] = 50
ordered_dict['item3'] = 20

print("Isi OrderedDict:")
for key, value in ordered_dict.items():
    print(key, ":", value)
# Fungsi: Menyimpan dan mencetak beberapa pasangan kunci-nilai dengan urutan.
# Kondisi: Ketika Anda perlu menjaga urutan saat menyimpan data terkait.
