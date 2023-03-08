def main():
    input1 = int(input("Masukkan angka pertama: "))
    input2 = int(input("Masukkan angka kedua: "))

    hasil_jumlah = jumlahkan(input1, input2)
    hasil_kali = kalikan(input1, input2)

    print("Hasil tambah adalah:", hasil_jumlah)
    print("Hasil darab adalah:", hasil_kali)

def jumlahkan(*args):
    total = 0
    for arg in args:
        total += arg
    return total


def kalikan(*args):
    total = 1
    for arg in args:
        total *= arg
    return total


if __name__ == "__main__":
    main()

