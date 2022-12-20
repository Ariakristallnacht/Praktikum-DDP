inp = int(input("input nilai bilangan"))
total = 0
for i in range(inp):
    nilai = int(input("masukan nilai: "))
    total += nilai
 
ratarata = total / inp

print("rata rata: ", ratarata)


#inp,total,nilai, dan ratarata merupakan variabel
#int adalah initeger yang berfungsi untuk meengubah data string menjadi integer(angka)
#input merupakan fungsi untuk menginput data
#for merupakan salah satu perintah perulangan
#i merupakan variabel yang di ambil dari range
#range merupakan fungsi yang menghasilkan rentan nilai tertentu
#end berfungsi agar tidak membuat baris baru ketika print()
#print() berfungsi untuk mencetak hasil
#+= berfungsi untuk menjumlahkan variabel sebelumnya dengan variabel lain
