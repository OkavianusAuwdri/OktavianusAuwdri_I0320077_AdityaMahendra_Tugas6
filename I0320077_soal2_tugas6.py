# Soal 2
z = 1
while z < 3:
    w = int(input("Masukan nilai: "))
    print("nilai ke-{} adalah: ".format(z), w)
    z = z + 1
    x = int(input("Masukan nilai: "))
    print("nilai ke-{} adalah: ".format(z), x)
    z = z + 1
    y = int(input("Masukan nilai: "))
    print("nilai ke-{} adalah: ".format(z), y)
    print("Nilai rata - ratanya adalah: ", (w + x + y)/3)
