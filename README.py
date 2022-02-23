print(30*"-")
print(" rumus bangun datar sederhana")
print("-"*30)
operator = input("masukkan luas bangun datar yang diinginkan : ")

if operator =="keliling persegi":
    sisi = int(input("masukkan angka:\t"))
    soal = sisi + sisi + sisi + sisi
    print(f"hasil dari keliling persegi adalah : {soal}")

elif operator =="luas persegi":
    sisi = int(input("masukkan angka:\t"))
    soal = sisi * sisi
    print(f"hasil dari luas persegi adalah : {soal}")

elif operator =="keliling persegi panjang":
    panjang = int(input("masukkan angka panjang:\t"))
    lebar = int(input("masukkan angka lebar :\t"))
    soal = (panjang + lebar) * 2
    print(f"hasil dari keliling persegi panjang adalah : {soal}")

elif operator =="luas persegi panjang":
    panjang = int(input("masukkan angka panjang:\t"))
    lebar = int(input("masukkan angka lebar :\t"))
    soal = panjang * lebar
    print(f"hasil dari keliling persegi panjang adalah : {soal}")

elif operator =="luas jajar genjang":
    alas = int(input("masukkan angka alas:\t"))
    tinggi = int(input("masukkan angka tinggi:\t"))
    soal = alas * tinggi
    print(f"hasil dari luas jajar genjang adalah : {soal}")

elif operator =="keliling jajar genjang":
    AB = int(input("masukkan angka : "))
    BC = int(input("masukkan angka : "))
    CD = int(input("masukkan angka : "))
    AD = int(input("masukkan angka : "))
    soal = AB + BC + CD + AD
    print(f"hasil dari keliling jajar genjang adalah {soal}")

elif operator =="luas trapesium":
    sisi_lebar = int(input("masukkan angka sisi lebar:\t"))
    tinggi = int(input("masukkan angka tinggi :\t"))
    soal = sisi_lebar * tinggi * 1 / 2
    print(f"hasil dari luas trapesium adalah : {soal}")


elif operator =="keliling trapesium":
    AB = int(input("masukkan angka : "))
    BC = int(input("masukkan angka : "))
    CD = int(input("masukkan angka : "))
    AD = int(input("masukkan angka : "))
    soal = AB + BC + CD + AD
    print(f"hasil dari keliling jajar genjang adalah {soal}")

elif operator =="luas layang layang":
    d1 = int(input("masukkan angka d1:\t"))
    d2 = int(input("masukkan angka d2:\t"))
    soal = d1 * d2 * 1 / 2
    print(f"hasil dari luas layang layang adalah : {soal}")

elif operator =="keliling layang layang":
    AB = int(input("masukkan angka : "))
    BC = int(input("masukkan angka : "))
    soal = 2*(AB+BC)
    print(f"hasil dari keliling layang layang adalah : {soal}")

elif operator =="luas segitiga":
    alas = int(input("masukkan angka alas:\t"))
    tinggi = int(input("masukkan angka tinggi:\t"))
    soal = alas * tinggi / 2
    print(f"hasil luas segitiga adalah : {soal}")

elif operator =="keliling segitiga":
    AB = int(input("masukkan angka : "))
    BC = int(input("masukkan angka : "))
    AC = int(input("masukkan angka : "))
    soal = AB + BC + AC
    print(f"hasil dari keliling segitiga adalah : {soal}")

else:
    print("""
    maaf kata kunci yang anda masukkan tidak tersedia atau salah ketik\n
    terima kasih T_T""")
