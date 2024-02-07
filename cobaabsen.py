#Program Absensi Mahasiswa (Tugas Besar UAS)

# Variabel penyimpan data mahasiswa
absensi_mahasiswa = [
    ['Mohammad Rangga Irghivya', 'Hadir'],
    ['Moch Nafis Azhar', 'Hadir'],
    ['Rafi Rifaldi', 'Izin'],
    ['Azka Muhammmad Zharfan', 'Tidak hadir'],
    ['Sean Julian Leo', 'Izin'],
    ['Dzulfikar Sadid', 'Tidak hadir'],
    ['Raffy Rachman', 'Tidak hadir']
]

# Fungsi untuk menambah data absensi mahasiswa
def tambah_absen(nama,kehadiran):
    absensi_mahasiswa.append([nama,kehadiran])

# Fungsi untuk menampilkan semua data
def lihat_absen() :
    for i in absensi_mahasiswa :
        print (f"{i[0]} : {i[1]}")

# Fungsi Pengurutan Naik
def Max_Sort_Naik(data,n):
    for i in range(n-1,0,-1):
        imax = i
        for j in range(i-1,-1,-1): 
            if data[j] [0] > data[imax] [0]:
                imax = j
        temp = data[i]
        data[i] = data[imax]
        data[imax] = temp

# Fungsi Pengurutan Turun
def Max_Sort_Turun(data,n):
    for i in range(n-1,0,-1):
        imax = i
        for j in range(i-1,-1,-1): 
            if data[j] [0] < data[imax] [0]:
                imax = j
        temp = data[i]
        data[i] = data[imax]
        data[imax] = temp

def pencarianNama (nama, data):
    L = 0
    R = len(data) - 1
    C = (L + R) // 2
    while (L <= R) and (data[C] [0] != nama):
        if data[C] [0] > nama:
            R = C - 1
        elif data[C] [0] < nama:
            L = C + 1    
        C = (L + R) // 2
    if data[C] [0] == nama:
        return C
    else:
        return -1
        

            
# Fungsi menampilkan menu utama
print ("----------------------------------------------")
print ("|         Porgram Absensi Mahasiswa          |")
print ("----------------------------------------------")
print ("Menu : ")
print ("1. Tambah Absensi ")
print ("2. Lihat Daftar Absensi ")
print ("3. Pengurutan Absensi Mahasiswa Berdasarkan ABC")
print ("4. Pengurutan Absensi Mahasiswa Berdasar ABC")
print ("5. Pencarian Absensi Mahasiswa")
print ("0. Keluar ")

while True :
    
    print()

    pilihan = input("Masukan pilhan anda : ")

    # Kondisi User saat memilih pilihan
    if pilihan == '1' :
        nama = input("Masukan Nama :")
        kehadiran = input("Masukan Kehadiran / Tidak Hadir / Izin / Hadir : ")
        tambah_absen(nama,kehadiran)
    
    elif pilihan == '2' :
        print ("Absensi : ")
        lihat_absen()

    elif pilihan == '3' :
        print ("Pengurutan berdasarkan kehadiran ")
        Max_Sort_Naik(absensi_mahasiswa,len(absensi_mahasiswa))
        lihat_absen()

    elif pilihan == '4' :
        print ("Pengurutan berdasarkan kehadiran ")
        Max_Sort_Turun(absensi_mahasiswa,len(absensi_mahasiswa))
        lihat_absen()

    elif pilihan == '5':
        dicari = input('Masukkan nama yang ingin dicari : ')
        Max_Sort_Naik(absensi_mahasiswa, len(absensi_mahasiswa))
        posisi = pencarianNama(dicari, absensi_mahasiswa)
        if posisi >= 0:
            print(f'Nama yang ditemukan {absensi_mahasiswa[posisi][0]} : {absensi_mahasiswa[posisi][1]}')
        else:
            print('Nama tidak ditemukan')
            
    elif pilihan == '0' :
        break