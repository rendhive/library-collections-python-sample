import collections

sentence = "The quick brown fox jumps over the lazy dog"
words = sentence.lower().split()
word_count = collections.Counter(words)

print("Jumlah kata dalam kalimat:", word_count)
# Fungsi: Menghitung jumlah kemunculan setiap kata dalam kalimat.
# Kondisi: Ketika Anda ingin menganalisis teks untuk kata yang sering muncul.
