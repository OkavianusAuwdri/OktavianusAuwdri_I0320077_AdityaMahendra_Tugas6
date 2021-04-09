# Soal 3
awal = 10
akhir = 24
for num in range(awal, akhir + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "bukan prima")
                break
        else:
            print(num, "adalah bilangan prima")
