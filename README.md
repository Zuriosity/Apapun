meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            }
for i in range (5):
    word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")
    
    if word in meme_dict.keys():
        print(meme_dict[word])
        # Apa yang harus kita lakukan jika kata itu ditemukan?
    else:
        # Apa yang harus kita lakukan jika kata itu tidak ditemukan?
        print('kata belum tersedia')
