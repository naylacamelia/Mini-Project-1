print("==================================")
print("________MINI PROJECT DDP 1________")
print("Nama: Nayla camelia indraswari")
print("NIM: 2409116009")
print("Kelas: A")
print("==================================")

#mendefinisikan nama dan nim yang akan diinput
nama1 = "nayla"
nim1 = 2409116009

#membuat input login user 
nama = str(input("\nMasukkan nama anda: "))
nim = int(input("Masukkan NIM anda: "))

#membuat pengulangan apabila user melakukan kesalahan input 
while True:
    if (nama == nama1 and nim == nim1) :
        print("Halo, Selamat datang, " + nama + "!")
        break #keluar dari loop jika login berhasil
    else:
        print("Nama atau NIM yang anda masukkan salah.")
        login_ulang = str(input("\nApakah anda ingin login kembali? (ya/tidak)"))        
        if login_ulang == "ya":
            nama = str(input("Masukkan nama anda: "))                           
            nim = int(input("Masukkan NIM anda: "))  
        else:  
            exit() #keluar dari program

while True:

    #memasukan jam kerja dan tarif kerja
    jam_kerja = float(input("\nMasukkan durasi jam kerja anda: "))
    tarif_kerja = float(input("Masukkan besaran tarif kerja per jam: "))
    
    gaji = jam_kerja * tarif_kerja

    if jam_kerja > 160: #kondisi apabila jam kerja lebih dari 160 jam
        bonus = gaji * 0.1 #menghitung bonus yang akan didapatkan
        gaji_total = gaji + bonus #menghitung total gaji setelah diberi bonus
        print("__________________________________________________________________")
        print("Bonus yang anda terima sebesar Rp." + str(bonus))
        print("Total gaji yang anda terima adalah sebesar Rp." + str(gaji_total))
        print("__________________________________________________________________")
    else:
        print("Gaji yang anda dapatkan adalah sebesar Rp." + str(gaji))

    pilihan = str(input("\nApakah anda ingin menghitung gaji kembali? (ya/tidak): "))
    if pilihan == "tidak":
        print("Program Selesai!") 
        break #keluar dari loop jika tidak ingin menghitung gaji kembali
    elif pilihan == "ya":
        continue #pengulangan untuk kembali menghitung gaji
    else:
        print("pilihan tidak tersedia.")

