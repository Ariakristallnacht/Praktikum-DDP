number1 = 5
number2 = 10

#operator perbandingan
if number1 != number2:
    print("Nomor berbeda!")
else:
    print("Nomor sama!")

#operator logika
if number1 > 99 and number2 < 1000:
    print("Bilangan ratusan!")
else:
    print("Bukan bilangan ratusan!")

#operator aritmatika
while True:
    number3 = int(input("Masukan angka: "))

    if number3 == 00:
        break
    
    if number3 % 2 == 0:
        print("Bilangan genap")
        
    else:
        print("Bilangan ganjil")
